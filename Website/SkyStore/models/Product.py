__author__ = 'bog02'

CATEGORY = [('Default', 'Default'), ('Children', 'Children'), ('Womens', 'Womens'), ('Mens', 'Mens')]

from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location=settings.STATIC_ROOT)


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=14)
    product_image = models.ImageField(upload_to="/static/media/", storage=fs, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, default='default')
    # Dimensions
    # Weight
    # Brand

    def get_product_stock_level(self):
        return len(self.productitem_set.filter(status="not_ordered"))

    @property
    def available(self):
        return self.get_product_stock_level() > 0

    class Meta:
        app_label = 'SkyStore'
        db_table = 'product'
