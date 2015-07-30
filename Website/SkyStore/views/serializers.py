__author__ = 'bog02'

from Website.SkyStore.models.Order import Order
from django.contrib.auth.models import User
# from Website.SkyStore.models.Customer import Customer
from Website.SkyStore.models.Address import Address
from Website.SkyStore.models.Store import Store
from Website.SkyStore.models.Product import Product
from Website.RewardsApp.models import Reward
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.core import exceptions


class RewardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reward
        fields = (
            'points'
        )


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = (
            'street_line1'
        )


class CustomerSerializer(serializers.ModelSerializer):

    address = serializers.StringRelatedField(many=True)
    user_reward = serializers.PrimaryKeyRelatedField(read_only=True)
    # addresses = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'address',
            'user_reward',
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
            'product_image',
            'available',
        )


class AuthCustomTokenSerializer(serializers.Serializer):
    email_or_username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        email_or_username = attrs.get('email_or_username')
        password = attrs.get('password')

        print email_or_username
        print password

        if email_or_username and password:
            user = authenticate(username=email_or_username, password=password)
            print "HELLO",user
            if user:
                if not user.is_active:
                    print "User is not active"
                    msg = 'User account is disabled.'
                    raise exceptions.ValidationError(msg)
            else:
                msg = 'Unable to log in with provided credentials.'
                raise exceptions.ValidationError(msg)
        else:
            msg = 'Must include "email or username" and "password"'
            raise exceptions.ValidationError(msg)
        print "end of function"
        attrs['user'] = user
        print "attrs:", attrs
        return attrs
