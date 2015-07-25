__author__ = 'bog02'


from django.db import models
from PaymentMethod import PaymentMethod


class Payment(models.Model):

    payment_method = models.OneToOneField(PaymentMethod, default=None)
    discount = models.DecimalField(max_length=20, decimal_places=2)

    class Meta:
        app_label = 'SkyStore'
        db_table = 'payment'


