__author__ = 'bog02'

from django.db import models


class PaymentMethod(models.Model):
    # card_type = models.CharField(max_length=4, default="card")

    class Meta:
        abstract = True
