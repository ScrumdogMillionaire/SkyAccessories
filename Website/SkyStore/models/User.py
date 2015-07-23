__author__ = 'bog02'


from django.db import models
from django.contrib.auth.models import User


class Login(models.Model):
    user = models.OneToOneField(User)

    # we could use json field for addresses
    addresses = models.ForeignKey('Address')

    class Meta:
        app_label = 'SkyStore'
        db_table = 'logins'

