from django.urls import path,include
from.views import *


urlpatterns = [
    
    path('country',CountryListApi.as_view()),
    path('country/<slug:slug>',CountryDetailApi.as_view()),
    path('orders/<int:user_id>',UserOrdersView.as_view()),
    path('add-order',OrderApiView.as_view()),
    path('increasebalance',IncreaseBalanceApiView.as_view()),
    path('balance/<int:user_id>',IncreaseBalanceApiView.as_view()),

  
    

]