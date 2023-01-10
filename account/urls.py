from django.urls import path,include
from.views import *




urlpatterns = [
    path('login',Login.as_view()),
    path('register',RegisterApiView.as_view()),
    path('profile/<int:pk>',UserDetail.as_view()),
    path('profile/me',CurrentUser.as_view()),
    path('logout',LogoutView.as_view()),

     

    path('country',CountryListApi.as_view()),
    path('country/<slug:slug>',CountryDetailApi.as_view()),


    




    
     
    # path('logout',LogoutView.as_view()),
    # path('users',UserListApiView.as_view()),
    # path('users/<int:pk>',UserDetailApiView.as_view()),

]