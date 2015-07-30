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
from . import serializers

from django.contrib.auth.models import User

# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


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

        serialized_product = ProductSerializer(product)
        return Response(serialized_product.data)


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
        user_id = User.objects.only('id').get(username=user).id

        content = {
            'token': unicode(token.key),
            'user': user_id,
        }

        return Response(content)


class ProcessOrderController(APIView):

    renderer_classes = (renderers.JSONRenderer,)

    def post(self, request):

        product = Product.objects.get(pk=request.data.get('prod_id'))
        customer = User.objects.get(id=request.data.get('user_id'))
        Order.objects.create(user=customer, price=product.get_price(), status='Order Placed')

        content = {'status': 'OK'}

        return Response(content)