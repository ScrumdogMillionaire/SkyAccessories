__author__ = 'bog02'

from django.contrib.auth.models import AbstractUser


class StaffLogin(AbstractUser):

    class Meta:
        app_label = 'SkyStore'
        db_table = 'staff_login'

