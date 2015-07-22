__author__ = 'bog02'


from django.db import models


class Address(models.Model):
    # TYPES = ['delivery', 'billing']
    # type = models.CharField(_('Type'), maxlength=20, choices = TYPES)

    street_line1 = models.CharField(max_length=100, null=True)
    street_line2 = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    county = models.CharField(max_length=100, null=True)
    postcode = models.CharField(max_length=8, null=True)

    class Meta:
        app_label = 'SkyStore'
        db_table = 'address'

