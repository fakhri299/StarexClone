from django.shortcuts import render
from.serializers import *
from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.generics import ListCreateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView,RetrieveAPIView
from.models import *


class CountryDetailApi(RetrieveAPIView):
    serializer_class=CountryDetailSerializer
    queryset=Country.objects.all()
    lookup_field='slug'



class CountryListApi(ListAPIView):
    serializer_class=CountrySerializer
    queryset=Country.objects.all()
    