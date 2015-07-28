__author__ = 'bog02'

from Basket import Basket
from django.db import models
from Website.SkyStore.models.ProductItem import ProductItem
from django.contrib.auth.models import User


class ShoppingBag(Basket, models.Model):
    contents = models.ForeignKey(ProductItem, null=True)
    user = models.OneToOneField(User, null=True)

    class Meta:
        app_label = 'SkyStore'
        db_table = 'shopping_bag'
