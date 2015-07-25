from django.contrib import admin

from models.Address import Address
# from models.CancelOrder import CancelOrder
# from models.Customer import Login
from models.Order import Order
from models.Product import Product
from models.ProductItem import ProductItem

models = [Order, Address, Product, ProductItem]
# admin.site.register(models)
