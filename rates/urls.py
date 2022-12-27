from django.urls import path,include
from.views import *


urlpatterns = [
    path('<slug:country_slug>',RateApi.as_view())
]
