__author__ = 'bog02'


from Website.SkyStore.models.Order import Order
from Website.SkyStore.views.serializers import OrderSerializer
# from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response


class OrderList(APIView):

    def get(self, request, format=None):
        orders = Order.objects.filter(status='Order Placed')
        serialized_orders = OrderSerializer(orders, many=True)
        return Response(serialized_orders.data)

