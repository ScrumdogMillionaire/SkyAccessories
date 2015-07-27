"""sky URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^home/', 'SkyStore.views.AccountController.home', name='home'),
    url(r'^index/', 'SkyStore.views.TestController.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', 'SkyStore.views.TestController.register', name='register'),
    url(r'^myaccount/', 'SkyStore.views.TestController.myaccount', name='myaccount'),
    url(r'^login/', 'SkyStore.views.TestController.login', name="login"),
    url(r'^accountsettings/', 'SkyStore.views.TestController.accountsettings', name="accountsettings"),

    #url(r'^all/$', 'SkyStore.views.TestController.products', name="products"),
    #url(r'^get/(?P<product_id>\d+)/$', 'SkyStore.views.TestController.product, name="product"),
]