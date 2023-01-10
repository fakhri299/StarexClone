from .models import *
from rest_framework.serializers import ModelSerializer



class ProfileSerializer(ModelSerializer):
    class Meta:
        model=Profile
        exclude=['user']



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

