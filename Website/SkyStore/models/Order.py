__author__ = 'bog02'

from django.db import models
from Customer import Customer


class Order(models.Model):

    STATUSES = [('Order Placed', 'Order Placed'), ('Out for Delivery', 'Out for Delivery'), ('Delivered', 'Delivered')]
    # status = models.BooleanField(default=False)

    creation_date = models.DateField(default=None)  # Creation Date of Order
    completed_date = models.DateField(default=None)  # Order Delivery Date
    expected_delivery_date = models.DateField(default=None)  # Expected Delivery Date

    status = models.CharField(max_length=20, choices=STATUSES)  # Status of Order
    user = models.ForeignKey(Customer, default=None)  # User who the order belongs to
    price = models.DecimalField(decimal_places=2, max_digits=14)

    def get_delivery_address(self):
        # Returns a delivery address for an order
        # return self.user.get_delivery_address()
        pass

    def calculate_order_price(self):
        # Returns the total price of an order
        total_price = 0
        for i in self.productItem_set.all():
            total_price += i.price

        return total_price

    def get_items(self):
        # Returns items for an order
        return self.productItem_set.all()

    class Meta:
        app_label = 'SkyStore'
        db_table = 'order'
