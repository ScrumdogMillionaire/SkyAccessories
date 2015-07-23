__author__ = 'bog02'


from django.db import models


class Payment(models.Model):
    payment_method = 0
    discount = 0

    def __init__(self, p_method):
        self.payment_method = p_method

