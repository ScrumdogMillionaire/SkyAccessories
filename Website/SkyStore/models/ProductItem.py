__author__ = 'bog02'

from django.db import models
from Website.SkyStore.models.Product import Product
from Website.SkyStore.models.Order import Order


class ProductItem(models.Model):
    serial_number = models.CharField(max_length=20)
    product = models.ForeignKey(Product, default=None)
    order = models.ForeignKey(Order, default=None)

    class Meta:
        app_label = 'SkyStore'
        db_table = 'product_item'
