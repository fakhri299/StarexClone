from django.shortcuts import render
from.serializers import *
from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView,GenericAPIView
from rest_framework.generics import ListCreateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView,RetrieveAPIView
from.models import *
from rest_framework.views import APIView
from rest_framework.response import Response 


class CountryDetailApi(RetrieveAPIView):
    serializer_class=CountryDetailSerializer
    queryset=Country.objects.all()
    lookup_field='slug'



class CountryListApi(ListAPIView):
    serializer_class=CountrySerializer
    queryset=Country.objects.all()
    



class OrderApiView(ListCreateAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(customer=user)


class UserOrdersView(GenericAPIView):
    serializer_class=OrderSerializer
    queryset=Order.objects.all()

    def get(self,request,user_id):
        customer=User.objects.get(id=user_id)

        orders=Order.objects.all().filter(customer=customer)

        serializer=self.serializer_class(instance=orders,many=True)

        return Response(serializer.data)



class IncreaseBalanceApiView(ListCreateAPIView):
    queryset=IncreaseBalance.objects.all()
    serializer_class=IncreaseBalanceSerializer

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(owner=user)


class UserBalanceView(GenericAPIView):
    serializer_class=IncreaseBalanceSerializer
    queryset=IncreaseBalance.objects.all()

    def get(self,request,user_id):
        owner=User.objects.get(id=user_id)

        balance=IncreaseBalance.objects.all().filter(owner=owner)

        serializer=self.serializer_class(instance=balance,many=True)

        return Response(serializer.data)

     
    
       


