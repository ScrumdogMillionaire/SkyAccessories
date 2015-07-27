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
# from Website import SkyStore
from Website.SkyStore.views.ApiController import OrderListController
from Website.SkyStore.views.ApiController import StoreListController
from Website.SkyStore.views.ApiController import ProductListController
from Website.SkyStore.views.ApiController import AuthController


urlpatterns = [
    url(r'^$', 'SkyStore.views.AccountController.home', name='home'),
    url(r'^index/', 'SkyStore.views.TestController.index', name='index'),
    # url(r'^api/orders/$', api.OrderList.as_view()),
    # url(r'^api/orders/$', 'SkyStore.apis.api.OrderList.as_view()'),
    # url(r'^SkyStore/', include('SkyStore.urls')),
    # url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/orders/$', OrderListController.as_view()),
    url(r'^api/stores/$', StoreListController.as_view()),
    url('^api/product/(?P<prod_id>[0-9]+)$', ProductListController.as_view()),
    # url(r'^api/login/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/auth/$', AuthController.as_view(), name='authenticate'),
]
