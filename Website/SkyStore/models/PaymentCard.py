__author__ = 'bog02'

from django.db import models
from Website.SkyStore.models.PaymentMethod import PaymentMethod
from django.contrib.auth.models import User


class PaymentCard(PaymentMethod):

    start_date = models.DateField(default=None)
    end_date = models.DateField(default=None)
    card_type = models.CharField(null=True, max_length=20)
    card_number = models.PositiveIntegerField(max_length=16, null=True)
    csv = models.PositiveIntegerField(max_length=3, null=True)
    # user = models.OneToOneField(User)
    # user = models.OneToOneField(Customer)
    user = models.OneToOneField(User, null=True)

    def validate_card(self):
        pass

    class Meta:
        app_label = 'SkyStore'
        db_table = 'p_cards'
