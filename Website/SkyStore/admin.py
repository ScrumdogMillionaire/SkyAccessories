from django.contrib import admin

from models.Address import Address
from models.CancelOrder import CancelOrder
from models.GuestUser import GuestUser
from models.User import User
# from models.Order import Order
from models.NormalOrder import NormalOrder
from models.Product import Product
from models.ProductItem import ProductItem

models = [GuestUser, Address, Product, ProductItem]
admin.site.register(models)
