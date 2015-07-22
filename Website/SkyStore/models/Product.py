__author__ = 'bog02'

from django.db import models


class Product(models.Model):
    pass

    class Meta:
        app_label = 'SkyStore'
        db_table = 'product'


