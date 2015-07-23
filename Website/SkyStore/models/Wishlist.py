__author__ = 'bog02'

from Basket import Basket


class Wishlist(Basket):
    def __init__(self, *args):
        super(Wishlist, self).__init__(*args)

    class Meta:
        app_label = 'SkyStore'
        db_table = 'wishlist'

