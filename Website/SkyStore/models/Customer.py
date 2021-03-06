__author__ = 'bog02'


from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser


class Customer(AbstractBaseUser):

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        default=None
    )

    username = models.CharField(unique=True, max_length=40)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    @property
    def is_staff(self):
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        app_label = 'SkyStore'
        db_table = 'customer_login'

