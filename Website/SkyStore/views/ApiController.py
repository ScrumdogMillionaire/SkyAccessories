__author__ = 'bog02'

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework import parsers
from rest_framework import renderers

from serializers import OrderSerializer
from serializers import StoreSerializer
from serializers import ProductSerializer
from Website.SkyStore.models.Order import Order
from Website.SkyStore.models.Store import Store
from Website.SkyStore.models.Product import Product
from Website.RewardsApp.models import Reward
# from Website.RewardsApp.models import Reward
from PIL import Image
from . import serializers
from datetime import date, timedelta


from django.contrib.auth.models import User

# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
import requests


class OrderListController(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, format='json'):
        orders = Order.objects.all()
        serialized_orders = OrderSerializer(orders, many=True)
        return Response(serialized_orders.data)


class StoreListController(APIView):

    def get(self, request, format='json'):
        stores = Store.objects.all()
        serialized_stores = StoreSerializer(stores, many=True)
        return Response(serialized_stores.data)


class ProductListController(APIView):

    def get(self, request, prod_id, format='json'):

        try:
            product = Product.objects.get(pk=prod_id)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # product.product_image = str(product.product_image).replace("static/media/"," ")
        # image = Image(product.product_image)
        # product.product_image = image
        # print image
        print product.product_image
        serialized_product = ProductSerializer(product)
        print serialized_product.data
        return Response([serialized_product.data])


class AuthTokenController(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (
        parsers.FormParser,
        parsers.MultiPartParser,
        parsers.JSONParser,
    )

    renderer_classes = (renderers.JSONRenderer,)

    def post(self, request):
        serializer = serializers.AuthCustomTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        user = User.objects.only('id').get(username=user)

        user_id = user.id
        email = user.email
        username = user.username
        first_name = user.first_name
        last_name = user.last_name

        reward = Reward.objects.only('id').get(user_id=user.id)
        reward_points = reward.points

        content = {
            'token': unicode(token.key),
            'user_id': user_id,
            'email': email,
            'username': username,
            'first_name': first_name,
            'last_name': last_name,
            'reward_points': reward_points,
        }

        return Response([content])


class ProcessOrderController(APIView):

    permission_classes = (IsAuthenticated,)
    renderer_classes = (renderers.JSONRenderer,)

    def post(self, request):
        print request.data.get('prod_id')
        # curr_time = datetime.datetime.now().strftime("%y-%m-%d")
        product = Product.objects.get(pk=request.data.get('prod_id'))
        customer = User.objects.get(id=request.data.get('user_id'))
        reward = customer.user_reward
        reward.decrement_points(product.price*10)
        reward.save()
        order = Order.objects.create(user=customer, price=product.price, status='Order Placed', creation_date=date.today(), expected_delivery_date=timedelta(days=3)+date.today())
        product_item = product.productitem_set.filter(status="not_ordered")[0]
        product_item.status = "ordered"
        product_item.order = order
        product_item.save()

        send_simple_message(request.user, order)
        content = [{'status': 'OK'}]

        return Response(content)


class RewardController(APIView):

    def get(self, request, format='json'):
        rewards = Reward.objects.all()
        serialized_reward = OrderSerializer(rewards, many=True)
        return Response(serialized_reward.data)

    def post(self, request, format='json'):

        permission_classes = (IsAuthenticated,)
        points = request.data.get('points')

        reward = Reward.objects.get(user_id=request.data.get('user_id'))
        reward.decrement_points(decrement=int(points))
        reward.save()

        content = [{'status': 'OK'}]

        return Response(content)


def send_simple_message(customer, order):
    order_string = "Hi "+ customer.username+ ",\nYour order has been successfully placed.\nDate Order Placed: "+ str(order.creation_date) +"\nDelivery Date: "+ str(order.expected_delivery_date) +"\n"
    product_items = order.productitem_set.all()
    order.products = []
    for product_item in product_items:
        print product_item.id
        product = Product.objects.get(pk=product_item.product_id)

        if product not in order.products:
            product.quantity = 1
            order.products.append(product)
        else:
            order.products[order.products.index(product)].quantity += 1
    for i in order.products:
        order_string += "Name: "+ i.name + " : "+ unichr(163) + str(i.price) + "\n"
    order_string += "______________________\n"
    order_string += "Total cost: "+ unichr(163) + str(order.price)+"\n"
    order_string += "______________________\n\n"
    order_string += "Delivery Address:\n"
    address = get_delivery_address(customer)
    order_string += address.street_line1 +"\n"
    order_string += address.street_line2 +"\n"
    order_string += address.city +"\n"
    order_string += address.county +"\n"
    order_string += address.postcode +"\n\n"
    order_string+= "Thanks for your order."

    return requests.post(
       "https://api.mailgun.net/v3/sandbox2247e4430337465194da28f52b4e090b.mailgun.org/messages",
       auth=("api", "key-49ea010ba13f50e4b7c9bc12e258132b"),
       data={"from": "Mailgun Sandbox <postmaster@sandbox2247e4430337465194da28f52b4e090b.mailgun.org>",
             "to": customer.username+ " <"+customer.email+">",
             "subject": "Your order has been confirmed",
             "text": order_string})

def get_delivery_address(user):
    return user.address.filter(address_type='default').all()[0]
