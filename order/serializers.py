from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from.models import *
from account.serializers import UserSerializer



class DetailSerializer(ModelSerializer):
    class Meta:
        model=CountryDetail
        fields='__all__'



class CountryDetailSerializer(ModelSerializer):
    detail=DetailSerializer()
    class Meta:
        model=Country
        fields=['name','image','detail']


class CountrySerializer(ModelSerializer):
    class Meta:
        model=Country
        fields=['name','image']







class IncreaseBalanceSerializer(ModelSerializer):
    class Meta:
        model=IncreaseBalance
        fields='__all__'

    

class ProfileSerializer(ModelSerializer):
    class Meta:
        model=Profile
        fields='__all__'
