from django.contrib import admin
from django.conf.urls import url

from api.views import AccountView, AccountListView, ProductBuyView, WrongEndpointView

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^api/account/$', AccountListView.as_view(), name='account-list'),
    url(r'^api/account/(?P<id>[0-9]+)/$', AccountView.as_view(), name='account'),
    url(r'^api/account/(?P<id>[0-9]+)/product_buy/(?P<price>(\d)+)/$', ProductBuyView.as_view(), name='account'),
    url(r'^api/.*', WrongEndpointView.as_view(), name='wrong-endpoint'),
]
