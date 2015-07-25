from django.contrib import admin

from models.Address import Address

from models.Customer import Customer
from models.Order import Order
from models.Product import Product
from models.ProductItem import ProductItem


models = [Order, Product, ProductItem, Address, Customer]
admin.site.register(models)
