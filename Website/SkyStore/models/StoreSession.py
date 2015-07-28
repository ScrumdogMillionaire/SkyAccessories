__author__ = 'bog02'
from django.contrib.auth.models import User
from django.db import models
from Website.SkyStore.models.ShoppingBag import ShoppingBag
from Website.SkyStore.models.Wishlist import Wishlist


class StoreSession(models.Model):
    shopping_bag = models.OneToOneField(ShoppingBag)
    wishlist = models.OneToOneField(Wishlist)
    user = models.OneToOneField(Useer, null=True)

    def get_contents(self):
        return self.contents

    class Meta:
        app_label = 'SkyStore'
        db_table = 'store_session'
