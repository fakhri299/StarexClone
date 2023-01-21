from django.db import models
from django.contrib.auth import get_user_model
from account.models import CustomUser


User=get_user_model()

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    created=models.DateTimeField(auto_now_add=True,null=True)
    updated=models.DateTimeField(auto_now=True,null=True,)
    
    


    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'



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
        ('TL','tl'),
        ('USD','usd')
    )

    owner=models.ForeignKey(Profile,on_delete=models.SET_NULL,related_name='profile_balance',null=True)
    card_number=models.CharField(max_length=16,unique=True)
    born_date=models.CharField(max_length=4)
    amount=models.BigIntegerField()
    currency=models.CharField(max_length=3,choices=CURRENCY_CHOICES)
    


    def __str__(self):
        return f'{self.owner} , {self.amount} {self.currency}'



class Order(models.Model):
    customer=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='orders',null=True)
    product_link=models.URLField()
    qwantity=models.IntegerField()
    size=models.CharField(max_length=50)
    cargo_price=models.FloatField()
    product_price=models.FloatField()
    notes=models.TextField(blank=True)
    created=models.DateTimeField(auto_now_add=True)
    balance=models.ForeignKey(IncreaseBalance,on_delete=models.DO_NOTHING,null=True)



    class Meta:
        verbose_name_plural='Sifarişler'


    def __str__(self) -> str:
        return f'{self.product_link}'


