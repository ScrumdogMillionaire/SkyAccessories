__author__ = 'bog02'

import Order


class CancelOrder(Order):
    def __init__(self, request_date):
        self.request_date = request_date

    class Meta:
        app_label = 'SkyStore'
        db_table = 'cancel_order'
