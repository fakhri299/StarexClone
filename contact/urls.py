from django.urls import path
from.views import *
from.views import *


urlpatterns = [

    path('districts',DistrictApi.as_view()),
    path('districts/<slug:point_slug>',PointContactApi.as_view()),
    path('countries',CountryApi.as_view()),
    path('countries/<slug:country_slug>',ContactStorageApi.as_view()),
    

    
    

]
    
