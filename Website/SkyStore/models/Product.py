__author__ = 'bog02'

from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location=settings.STATIC_ROOT)

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=14)
    product_image = models.ImageField(upload_to="images", storage=fs, null=True)

    # Dimensions
    # Weight
    # Brand

    class Meta:
        app_label = 'SkyStore'
        db_table = 'product'
