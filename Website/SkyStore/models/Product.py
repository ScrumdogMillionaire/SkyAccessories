__author__ = 'bog02'

from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location=settings.STATIC_ROOT)


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=14)
    product_image = models.ImageField(upload_to="images", storage=fs)
    # Dimensions
    # Weight
    # Brand

    def get_product_stock_level(self):
        return len(Product.objects.all())

    @property
    def available(self):
        return self.get_product_stock_level() > 0

    class Meta:
        app_label = 'SkyStore'
        db_table = 'product'
