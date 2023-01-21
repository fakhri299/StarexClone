from .models import *
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from account.serializers import UserSerializer


User=get_user_model()


class ProfileSerializer(ModelSerializer):
    orders=serializers.StringRelatedField(many=True)
    class Meta:
        model=Profile
        fields=['orders','created','updated',]


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



class OrderSerializer(ModelSerializer):

    total_amount=serializers.SerializerMethodField()
    customer=serializers.StringRelatedField(read_only=True)
    

    class Meta:
        model=Order
        fields=['customer','product_link','qwantity','size',
                'size','cargo_price','product_price','total_amount','notes','created']

    def get_total_amount(self,obj):
        total=obj.qwantity * obj.product_price
        total_price=total+obj.cargo_price+14
        return total_price

   



class IncreaseBalanceSerializer(ModelSerializer):

    class Meta:
        model=IncreaseBalance
        fields=['card_number','amount','born_date','currency',]


