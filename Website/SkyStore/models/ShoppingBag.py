__author__ = 'bog02'

from Basket import Basket
from django.db import models
from django.contrib.auth.models import User


class ShoppingBag(Basket, models.Model):
    user = models.OneToOneField(User, null=True)

    def get_contents(self):
        return self.product_set.all()

    class Meta:
        app_label = 'SkyStore'
        db_table = 'shopping_bag'
