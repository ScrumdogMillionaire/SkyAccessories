__author__ = 'bog02'


from django.db import models
from ProductItem import ProductItem
from User import User


class Basket(models.Model):
    contents = models.ForeignKey(ProductItem, default=None)
    user = models.OneToOneField(User, default=None)

    def get_contents(self):
        return self.contents

    class Meta:
        abstract = True
