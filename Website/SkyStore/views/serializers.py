__author__ = 'bog02'

from Website.SkyStore.models.Order import Order
from django.contrib.auth.models import User
# from Website.SkyStore.models.Customer import Customer
from Website.SkyStore.models.Address import Address
from Website.SkyStore.models.Store import Store
from Website.SkyStore.models.Product import Product
from rest_framework import serializers


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = (
            'street_line1'
        )


class CustomerSerializer(serializers.ModelSerializer):

    address = serializers.StringRelatedField(many=True)
    # addresses = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'address'
        )


class OrderSerializer(serializers.ModelSerializer):

    user = CustomerSerializer()

    class Meta:

        model = Order
        fields = (
            'id',
            'creation_date',
            'expected_delivery_date',
            'user'
        )


class StoreSerializer(serializers.ModelSerializer):

    class Meta:

        model = Store
        fields = (
            'id',
            'description',
            'latitude',
            'longitude'
        )


class ProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = Product
        fields = (
            'name',
            'description',
            'price',
            'product_image'
        )

