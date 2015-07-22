__author__ = 'bog02'

from django.db import models
from django.contrib.auth.models import User


class GuestUser(models.Model):
    user = models.OneToOneField(User)
    addresses = models.ForeignKey('Address')

    class Meta:
        app_label = 'SkyStore'
        db_table = 'guest_user'

    def __init__(self):
        super(User, self).__init__()


