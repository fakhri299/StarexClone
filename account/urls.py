from django.urls import path,include
from.views import *



urlpatterns = [
    path('login',Login.as_view()),
    path('register',RegisterApi.as_view()),
    path('logout',LogoutView.as_view()),

]