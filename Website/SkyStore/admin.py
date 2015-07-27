from django.contrib import admin

from Website.SkyStore.models.Address import Address
# from models.CancelOrder import CancelOrder
# from Website.SkyStore.models.Customer import Customer
from Website.SkyStore.models.Order import Order
from Website.SkyStore.models.Product import Product
from Website.SkyStore.models.ProductItem import ProductItem


models = [Order, Product, ProductItem, Address]
admin.site.register(models)