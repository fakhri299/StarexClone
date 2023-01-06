from django.urls import path,include
from.views import *




urlpatterns = [
    path('country',CountryListApi.as_view()),
    path('country/<slug:slug>',CountryDetailApi.as_view()),


    path('profile/<int:pk>',ProfileDetailApi.as_view()),
    
]