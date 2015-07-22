__author__ = 'bog02'


from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=20)

    class Meta:
        app_label = 'SkyStore'
        db_table = 'address'

