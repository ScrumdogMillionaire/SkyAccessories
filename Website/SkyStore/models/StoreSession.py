__author__ = 'bog02'

from django.db import models
from Customer import User
from ShoppingBag import ShoppingBag
from Wishlist import Wishlist


class StoreSession(models.Model):
    shopping_bag = models.OneToOneField(ShoppingBag)
    wishlist = models.OneToOneField(Wishlist)
    user = models.OneToOneField(User, default=None)

    def get_contents(self):
        return self.contents

    class Meta:
        app_label = 'SkyStore'
        db_table = 'store_session'
