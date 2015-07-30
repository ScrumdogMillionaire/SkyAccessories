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
# from Website.SkyStore.views.ApiController import OrderListController

urlpatterns = [
    url(r'^$', 'SkyStore.views.TestController.home', name='home'),
    url(r'^index/', 'SkyStore.views.TestController.index', name='index'),
    url(r'^$', 'SkyStore.views.TestController.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', 'SkyStore.views.TestController.register', name='register'),
    url(r'^myaccount/', 'SkyStore.views.TestController.myaccount', name='myaccount'),
    url(r'^login/', 'SkyStore.views.TestController.login', name="login"),
    url(r'^loginuser/', 'SkyStore.views.TestController.loginuser', name="loginuser"),
    url(r'^logout/', 'SkyStore.views.TestController.logout_view', name="logout"),
    url(r'^accountsettings/', 'SkyStore.views.AccountController.accountsettings', name="accountsettings"),
    url(r'^basket/', 'SkyStore.views.BasketController.basket', name="basket"),
    url(r'^addtobasket/$', 'SkyStore.views.BasketController.add_to_basket', name="addtobasket"),
    url(r'^removefrombasket/(?P<product_id>\d+)/$', 'SkyStore.views.BasketController.remove_from_basket', name="removefrombasket"),
    url(r'^increasequantity/(?P<product_id>\d+)/$', 'SkyStore.views.BasketController.increase_quantity', name="increasequantity"),
    url(r'^productlist/', 'SkyStore.views.TestController.productlist', name="productlist"),
    url(r'^adminpage/', 'SkyStore.views.TestController.adminpage', name="adminpage"),
    url(r'^addproductpage/', 'SkyStore.views.TestController.addproductpage', name="addproductpage"),
    url(r'^addproduct/', 'SkyStore.views.TestController.addproduct', name="addproduct"),
    # url(r'^api/orders/$', OrderListController.as_view()),

    #url(r'^all/$', 'SkyStore.views.TestController.products', name="products"),
    url(r'^search/', 'SkyStore.views.ProductController.search', name="search"),
    url(r'^checkout/', 'SkyStore.views.ProductController.checkout', name="checkout"),
    url(r'^revieworder/', 'SkyStore.views.ProductController.review_order', name="revieworder"),
    url(r'^successfulorder/', 'SkyStore.views.ProductController.successful_order', name="successfulorder"),
    #url(r'^all/$', 'SkyStore.views.TestController.products', name="products"),
    url(r'^product/(?P<product_id>\d+)/$', 'SkyStore.views.ProductController.product_handler', name="product"),
]
