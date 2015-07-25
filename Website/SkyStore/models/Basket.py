__author__ = 'bog02'


from django.db import models
from Website.SkyStore.models.ProductItem import ProductItem
from Website.SkyStore.models.Customer import Customer


class Basket(models.Model):
    contents = models.ForeignKey(ProductItem, default=None)
    user = models.OneToOneField(Customer, default=None)

    def get_contents(self):
        return self.contents

    class Meta:
        abstract = True
