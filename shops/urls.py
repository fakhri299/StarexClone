from django.urls import path,include
from .views import ShopListApiView,ShopByCategoryApiView,CountryApi

urlpatterns = [
    path('countries',CountryApi.as_view()),
    path('',ShopListApiView.as_view()),
    path('<slug:slug>',ShopByCategoryApiView.as_view()),
    
]