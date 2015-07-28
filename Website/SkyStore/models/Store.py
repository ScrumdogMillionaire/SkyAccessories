__author__ = 'bog02'


from django.db import models


class Store(models.Model):

    description = models.CharField(max_length=200, default=None)
    longitude = models.CharField(max_length=10, default=None)
    latitude = models.CharField(max_length=10, default=None)

    class Meta:
        app_label = 'SkyStore'
        db_table = 'store_coordinates'
