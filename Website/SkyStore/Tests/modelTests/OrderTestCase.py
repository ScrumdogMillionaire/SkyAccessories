from django.test import TestCase
from Website.SkyStore.models.Order import Order


class OrderTestCase(TestCase):
    def setUp(self):
        order_one = Order.objects.create(creation_date=None, completed_date=None,completed_date=None,
                                         expected_delivery_date=None, status=None, user=None, price=None)

    def test_get_delivery_address(self):
        pass