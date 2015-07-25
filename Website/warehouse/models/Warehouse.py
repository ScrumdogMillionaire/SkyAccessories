__author__ = 'bog02'


from django.db import models


class Warehouse(models.Model):
    pass

    class Meta:
        app_label = 'Warehouse'
        db_table = 'warehouse'
