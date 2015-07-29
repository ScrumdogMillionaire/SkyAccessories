# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SkyStore', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingbag',
            name='user',
        ),
        migrations.AddField(
            model_name='productitem',
            name='status',
            field=models.CharField(default=b'not_ordered', max_length=20, null=True, choices=[(b'not_ordered', b'not_ordered'), (b'ordered', b'ordered')]),
        ),
        migrations.DeleteModel(
            name='ShoppingBag',
        ),
    ]
