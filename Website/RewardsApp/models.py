__author__ = 'bog02'

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Reward(models.Model):

    points = models.IntegerField(default=0)
    user = models.OneToOneField(User, null=True, related_name='user_reward')

    class Meta:
        app_label = 'SkyStore'
        db_table = 'rewards'

    def get_reward_points(self):
        return self.points

    def decrement_points(self, decrement):
        self.points = self.points - decrement

    def get_cash_equivalent(self):
        return self.points/100

