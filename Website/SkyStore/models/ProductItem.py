__author__ = 'bog02'

from django.db import models
# from Product import Product
# from Order import Order

STATUS = [('not_ordered', 'not_ordered'), ('ordered', 'ordered'), ('removed','removed')]


class ProductItem(models.Model):
    status = models.CharField(max_length=20, choices=STATUS, null=True, default='not_ordered')
    serial_number = models.CharField(max_length=20)
    product = models.ForeignKey('Product', null=True)
    order = models.ForeignKey('Order', null=True)

    def order_item(self):
        self.status = 'ordered'

    class Meta:
        app_label = 'SkyStore'
        db_table = 'product_item'