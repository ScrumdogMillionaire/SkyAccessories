__author__ = 'bog02'

import datetime
from django.db import models
from PaymentMethod import PaymentMethod
from Customer import User


class PaymentCard(PaymentMethod):

    start_date = models.DateField(default=None)
    end_date = models.DateField(default=None)
    # card_type = models.CharField()
    # start_date = start_date
    # end_date = end_date
    # cvv = cvv
    user = models.OneToOneField(User)

    def validate_card(self):
        pass

    class Meta:
        app_label = 'SkyStore'
        db_table = 'p_cards'
