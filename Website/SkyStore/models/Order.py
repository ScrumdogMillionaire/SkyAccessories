__author__ = 'bog02'

from django.db import models


class Order(models.Model):
    status = models.BooleanField(default=False)
    completed_date = models.DateField

    def get_status(self):
        return self.status

    class Meta:
        abstract = True
