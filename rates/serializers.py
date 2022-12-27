from.models import *
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers




class TarifSerializer(ModelSerializer):
    class Meta:
        model=Tarif
        exclude=['countryandtype']

class CargoMethodSerializer(ModelSerializer):
    tarif=TarifSerializer(many=True)
    class Meta:
        model=RateType 
        fields='__all__'




class CountrySerializer(ModelSerializer):
    cargo_type=CargoMethodSerializer(many=True,)
    class Meta:
        model=Country
        fields='__all__'