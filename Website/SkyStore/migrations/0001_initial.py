# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address_type', models.CharField(default=b'default', max_length=20, choices=[(b'default', b'default'), (b'billing', b'billing')])),
                ('street_line1', models.CharField(max_length=100, null=True)),
                ('street_line2', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('county', models.CharField(max_length=100, null=True)),
                ('postcode', models.CharField(max_length=8, null=True)),
                ('user', models.ForeignKey(related_name='address', default=None, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation_date', models.DateField(null=True)),
                ('completed_date', models.DateField(null=True)),
                ('expected_delivery_date', models.DateField(null=True)),
                ('status', models.CharField(max_length=20, choices=[(b'Order Placed', b'Order Placed'), (b'Out for Delivery', b'Out for Delivery'), (b'Delivered', b'Delivered')])),
                ('price', models.DecimalField(max_digits=14, decimal_places=2)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('description', models.TextField()),
                ('price', models.DecimalField(max_digits=14, decimal_places=2)),
                ('product_image', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location=b'/Users/mpa45/SkyAccessories/Website/sky/static/'), null=True, upload_to=b'images')),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('serial_number', models.CharField(max_length=20)),
                ('order', models.ForeignKey(to='SkyStore.Order', null=True)),
                ('product', models.ForeignKey(to='SkyStore.Product', null=True)),
            ],
            options={
                'db_table': 'product_item',
            },
        ),
        migrations.CreateModel(
            name='ShoppingBag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'shopping_bag',
            },
        ),
        migrations.CreateModel(
            name='StaffLogin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.BooleanField(default=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'staff_login',
            },
        ),
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
    ]
