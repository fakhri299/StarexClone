from.models import *
from rest_framework.serializers import ModelSerializer


class CountrySerializer(ModelSerializer):
    class Meta:
        model=Country
        fields='__all__'


class ContactSerializer(ModelSerializer):
    country=CountrySerializer()
    class Meta:
        model=CountryContact
        fields='__all__'


class DistrictSerializer(ModelSerializer):
    class Meta:
        model=District
        fields='__all__'


class ContactPointSerializer(ModelSerializer):
    district=DistrictSerializer()
    class Meta:
        model=PointContact
        fields='__all__'




