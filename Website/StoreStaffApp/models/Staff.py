__author__ = 'bog02'

from django.db import models
from django.contrib.auth.models import User


class StaffLogin(models.Model):
    user = models.OneToOneField(User)

    # we could use json field for addresses
    status = models.BooleanField(default=True)

    class Meta:
        app_label = 'SkyStore'
        db_table = 'staff_login'
