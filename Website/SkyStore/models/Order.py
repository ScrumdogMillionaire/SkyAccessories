__author__ = 'bog02'

import abc
from django.db import models


class Order(object):
    __metaclass__ = abc.ABCMeta
    status = models.BooleanField(default=False)
    completed_date = models.DateField

    def get_status(self):
        return self.status

