__author__ = 'bog02'

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from serializers import OrderSerializer
from serializers import StoreSerializer
from serializers import ProductSerializer
from Website.SkyStore.models.Order import Order
from Website.SkyStore.models.Store import Store
from Website.SkyStore.models.Product import Product
from . import authentication, serializers


class OrderListController(APIView):

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


class AuthController(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CustomerSerializer

    def post(self, request, *args, **kwargs):
        return Response(self.serializer_class(request.user).data)

    def get(self, request, format=None):
        content = {
            'user': unicode(request.user),  # `django.contrib.auth.User` instance.
            'auth': unicode(request.auth),  # None
        }
        return Response(content)
