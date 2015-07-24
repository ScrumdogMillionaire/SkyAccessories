__author__ = 'bog02'

import datetime
from django.db import models
from PaymentMethod import PaymentMethod
from Customer import User


class PaymentCard(PaymentMethod):

    start_date = 0
    end_date = 0
    cvv = 0
    user = 0

    def __init__(self, card_type, start_date, end_date, cvv, *args):
        super(PaymentCard, self).__init__(*args)
        self.card_type = card_type
        self.start_date = start_date
        self.end_date = end_date
        self.cvv = cvv
        self.user = models.OneToOneField(User)

    def validate_card(self):
        pass

    class Meta:
        app_label = 'SkyStore'
        db_table = 'p_cards'
