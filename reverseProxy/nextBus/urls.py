from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^agencylist/', agencyList),
    url(r'^routelist/', routeList),
    url(r'^routeconfig/', routeConfig),
    url(r'^predictions/', prediction),
]
