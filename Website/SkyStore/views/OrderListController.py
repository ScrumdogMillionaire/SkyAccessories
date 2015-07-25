__author__ = 'bog02'

from rest_framework.views import APIView
from rest_framework.response import Response

from serializers import OrderSerializer
from Website.SkyStore.models.Order import Order


class OrderListController(APIView):

    def get(self, request, format='json'):
        orders = Order.objects.all()
        serialized_orders = OrderSerializer(orders, many=True)
        return Response(serialized_orders.data)

