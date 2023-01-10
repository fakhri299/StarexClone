from django.contrib.auth import get_user_model
from .models import *
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import ValidationError
from rest_framework.serializers import ModelSerializer




User=get_user_model()

class RegisterSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['id','first_name','last_name','gender','day','month','year','id_card_seria','fin_code','password','password_again','id_card_seria','id_card_number','telephon','email','district','adress','filial','promocode']
        extra_kwargs = {
            'password': {'write_only': True},
            'password_again': {'write_only': True},

        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password_again']:
            raise ValidationError('Passwords are not match')
        return attrs
        

        

    def create(self, validated_data):
        user = User.objects.create_user(
            first_name=validated_data['first_name'], 
            last_name=validated_data['last_name'], 
            gender=validated_data['gender'],
            telephon=validated_data['telephon'], 
            email=validated_data['email'], 
            district=validated_data['district'], 
            adress=validated_data['adress'],
            filial=validated_data['filial'],
            promocode=validated_data['promocode'],
            password=validated_data['password'],
            id_card_seria=validated_data['id_card_seria'],
            id_card_number=validated_data['id_card_number'],
            fin_code=validated_data['fin_code'],
            day=validated_data['day'],
            month=validated_data['month'],
            year=validated_data['year']
        )
        return user




class ProfileSerializer(ModelSerializer):
    class Meta:
        model=Profile
        exclude=['user']



class UserSerializer(ModelSerializer):
    profile=ProfileSerializer(read_only=True)
    class Meta:
        model=CustomUser
        fields=['id','profile','first_name','last_name','gender','telephon','email','district','adress','filial','promocode','day','month','year']
        extra_kwargs={
            'password':{'write_only':True}
        }



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





    

