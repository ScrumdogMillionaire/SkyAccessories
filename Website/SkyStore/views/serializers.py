__author__ = 'bog02'

from Website.SkyStore.models.Order import Order
# from Website.SkyStore.models.Customer import Customer
from django.contrib.auth.models import User

from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id'
        )


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        user = CustomerSerializer()
        model = Order
        fields = (
            'id',
            'creation_date',
            'expected_delivery_date',
            'user'
        )