from django.contrib import admin

from models.Address import Address
# from models.CancelOrder import CancelOrder
# from models.Customer import Login
from .models import Order
from .models import Product
from .models import ProductItem

models = [Order, Address, Product, ProductItem]
# admin.site.register(models)
