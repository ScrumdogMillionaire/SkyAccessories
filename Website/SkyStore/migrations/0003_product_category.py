# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SkyStore', '0002_auto_20150729_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default=b'default', max_length=20, choices=[(b'Default', b'Default'), (b'Children', b'Children'), (b'Womens', b'Womens'), (b'Mens', b'Mens')]),
        ),
    ]
