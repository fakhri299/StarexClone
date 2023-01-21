from django.shortcuts import render
from.serializers import *
from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView,GenericAPIView
from rest_framework.generics import ListCreateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView,RetrieveAPIView
from.models import *
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.generics import get_object_or_404


class CountryDetailApi(RetrieveAPIView):
    serializer_class=CountryDetailSerializer
    queryset=Country.objects.all()
    lookup_field='slug'



class CountryListApi(ListAPIView):
    serializer_class=CountrySerializer
    queryset=Country.objects.all()
    



class OrderApiView(CreateAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    

    def perform_create(self, serializer):
        profile=self.request.user.profile
        serializer.save(customer=profile)




class ProfileDetail(RetrieveUpdateDestroyAPIView):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer



class IncreaseBalanceApiView(CreateAPIView):
    serializer_class=IncreaseBalanceSerializer
    queryset=IncreaseBalance.objects.all()

    
    




   

       


