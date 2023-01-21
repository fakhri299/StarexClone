from django.urls import path,include
from.views import *


urlpatterns = [
    
    path('country',CountryListApi.as_view()),
    path('country/<slug:slug>',CountryDetailApi.as_view()),
    path('add-order',OrderApiView.as_view()),
    path('<int:pk>',ProfileDetail.as_view()),
    path('increase-balance',IncreaseBalanceApiView.as_view())
    

]