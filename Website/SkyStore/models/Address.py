__author__ = 'bog02'
TYPES = [('default', 'default'), ('billing', 'billing')]

from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):

    address_type = models.CharField(max_length=20, choices=TYPES, default='default')

    street_line1 = models.CharField(max_length=100, null=True)
    street_line2 = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    county = models.CharField(max_length=100, null=True)
    postcode = models.CharField(max_length=8, null=True)
    user = models.ForeignKey(User, related_name='address', default=None)

    class Meta:
        app_label = 'SkyStore'
        db_table = 'address'

    def __unicode__(self):              # __unicode__ on Python 2
        return "%s %s %s" % (self.street_line1, self.street_line2, self.city)
