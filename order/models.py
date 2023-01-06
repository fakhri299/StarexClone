from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxLengthValidator,MinLengthValidator


User=get_user_model()




class CountryDetail(models.Model):
    city=models.CharField(max_length=20,null=True,blank=True)
    phone=models.CharField(max_length=11,null=True,blank=True)
    adress=models.CharField(max_length=50,null=True,blank=True)
    adress2=models.CharField(max_length=50,null=True,blank=True)
    quarter=models.CharField(max_length=50,null=True,blank=True)
    district=models.CharField(max_length=50,null=True,blank=True)
    number=models.CharField(max_length=50,null=True,blank=True)
    post_code=models.CharField(max_length=50,null=True,blank=True)


    def __str__(self):
        return self.city


class Country(models.Model):
    name=models.CharField(max_length=20,null=True,blank=True)
    image=models.ImageField()
    slug=models.SlugField(max_length=10)
    detail=models.OneToOneField(CountryDetail,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name




class IncreaseBalance(models.Model):

    CURRENCY_CHOICES=(
        ('usd','USD'),
        ('tl','TL')
    )


    fullname=models.CharField(max_length=30,)
    card_number=models.PositiveIntegerField(validators=[MaxLengthValidator(16)])
    day_month=models.PositiveIntegerField(validators=[MaxLengthValidator(4),MinLengthValidator(2)])
    amount=models.PositiveIntegerField()
    currency=models.CharField(max_length=3,choices=CURRENCY_CHOICES)

    def __str__(self):
        return f'{self.fullname}-{self.card_number}'




class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')


    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
























