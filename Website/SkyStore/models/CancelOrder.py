__author__ = 'bog02'

import Order


class CancelOrder(Order):
    def __init__(self, request_date, *args):
        super(CancelOrder, self).__init__(*args)
        self.request_date = request_date

    class Meta:
        app_label = 'SkyStore'
        db_table = 'cancel_order'
