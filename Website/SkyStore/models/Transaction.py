__author__ = 'bog02'

from django.db import models


class Transaction(models.Model):

    def __init__(self, order, payment):
        self.order = order
        self.payment = payment



