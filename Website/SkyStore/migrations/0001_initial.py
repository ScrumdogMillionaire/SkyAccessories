# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


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
            ],
            options={
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('email', models.EmailField(default=None, unique=True, max_length=255, verbose_name=b'email address')),
                ('username', models.CharField(max_length=40, unique=True, serialize=False, primary_key=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'customer_login',
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
                ('user', models.ForeignKey(to='SkyStore.Customer', null=True)),
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
                ('product_image', models.ImageField(upload_to=b'')),
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
                ('order', models.ForeignKey(default=None, to='SkyStore.Order')),
                ('product', models.ForeignKey(default=None, to='SkyStore.Product')),
            ],
            options={
                'db_table': 'product_item',
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
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(default=None, to='SkyStore.Customer'),
        ),
    ]
