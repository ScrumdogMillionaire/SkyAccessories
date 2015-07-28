__author__ = 'bog02'


from django.db import models
from Website.SkyStore.models.ProductItem import ProductItem
from django.contrib.auth.models import User
# from Website.SkyStore.models.Customer import Customer


class Basket(models.Model):
    # contents = models.ForeignKey(ProductItem, null=True)
    # user = models.OneToOneField(User, null=True)

    def get_contents(self):
        return self.contents

    class Meta:
        abstract = True
