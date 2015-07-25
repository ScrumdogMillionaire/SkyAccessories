__author__ = 'bog02'

from Basket import Basket


class ShoppingBag(Basket):
    def __init__(self, *args):
        super(ShoppingBag, self).__init__(*args)

    class Meta:
        app_label = 'SkyStore'
        db_table = 'shopping_bag'
