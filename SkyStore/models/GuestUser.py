__author__ = 'bog02'

from django.db import models
from django.contrib.auth.models import User


class GuestUser(models.Model):
    user = models.OneToOneField(User)

    class Meta:
        app_label = 'SkyStore'
        db_table = 'guest_user'


