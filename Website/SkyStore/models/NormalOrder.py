__author__ = 'bog02'

import Order


class NormalOrder(Order):
    def __init__(self, create_date):
        self.create_date = create_date

    class Meta:
        app_label = 'SkyStore'
        db_table = 'normal_order'
