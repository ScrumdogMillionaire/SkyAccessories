# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('SkyStore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(default=None, max_length=200)),
                ('longitude', models.CharField(default=None, max_length=10)),
                ('latitude', models.CharField(default=None, max_length=10)),
            ],
            options={
                'db_table': 'store_coordinates',
            },
        ),
        migrations.RemoveField(
            model_name='stafflogin',
            name='user',
        ),
        migrations.AlterField(
            model_name='address',
            name='user',
            field=models.ForeignKey(related_name='address', default=None, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='StaffLogin',
        ),
    ]
