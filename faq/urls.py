from django.urls import path,include
from.views import *


urlpatterns = [
    path('questions',QuestionApi.as_view()),
    path('categories',CategoryApi.as_view()),    
    path('categories/<slug:slug>',QuestionbyategoryApi.as_view()),
     

]

