from .models import Shop,Country
from rest_framework.serializers import ModelSerializer

class CountrySerializer(ModelSerializer):
    class Meta:
        model=Country
        fields='__all__'


class ShopSerilizer(ModelSerializer):
    class Meta:
        model=Shop
        exclude=['country']


