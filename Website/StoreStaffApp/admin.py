from django.contrib import admin

from Website.StoreStaffApp.models.Staff import StaffLogin
# Register your models here.

models = [StaffLogin]
admin.site.register(models)
