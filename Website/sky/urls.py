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
from Website import SkyStore
# from Website.SkyStore.views.ApiController import Controller import OrderListController
from Website.SkyStore.views.ApiController import OrderListController
from Website.SkyStore.views.ApiController import StoreListController
from Website.SkyStore.views.ApiController import ProductListController
from Website.SkyStore.views.ApiController import AuthTokenController
from Website.SkyStore.views.ApiController import ProcessOrderController
from Website.SkyStore.views.ApiController import RewardController
from rest_framework.authtoken import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    url(r'^skystore/', include('SkyStore.urls')),
    url(r'^api/orders/$', OrderListController.as_view()),
    url(r'^api/stores/$', StoreListController.as_view()),
    url('^api/product/(?P<prod_id>[0-9]+)$', ProductListController.as_view()),
    url(r'^api-auth/', AuthTokenController.as_view()),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^api/place-order/', ProcessOrderController.as_view()),
    url(r'^api-rewards/', RewardController.as_view()),
    url(r'^api/reward/update/', RewardController.as_view()),

]

urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
