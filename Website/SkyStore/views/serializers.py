__author__ = 'bog02'

from Website.SkyStore.models.Order import Order
from rest_framework import serializers


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = (
            'id',
            'creation_date',
            'expected_delivery_date'
        )
