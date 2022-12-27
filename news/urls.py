from django.urls import path,include
from .views import NewsViewSet
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register(r'',NewsViewSet)

urlpatterns = [
   path('',include(router.urls))
]