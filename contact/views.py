from django.shortcuts import render
from rest_framework.generics import ListAPIView
from.serializers import *
from.models import *

# Create your views here.

class ContactStorageApi(ListAPIView):
    serializer_class=ContactSerializer


    def get_queryset(self):
        slug=self.kwargs.get('country_slug')
        return CountryContact.objects.filter(country__slug=slug)



class CountryApi(ListAPIView):
    queryset=Country.objects.all()
    serializer_class=CountrySerializer


class DistrictApi(ListAPIView):
    queryset=District.objects.all()
    serializer_class=DistrictSerializer


class PointContactApi(ListAPIView):
    serializer_class=ContactPointSerializer


    def get_queryset(self):
        slug=self.kwargs.get('point_slug')
        return PointContact.objects.filter(slug=slug)
