__author__ = 'bog02'

from django.db import models
from Order import Order


class CancelOrder(models.Model):
    request_date = models.DateField(default=None)
    order = models.OneToOneField(Order, default=None)

    class Meta:
        app_label = 'SkyStore'
        db_table = 'cancel_order'
