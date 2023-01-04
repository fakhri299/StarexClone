from django.db import models
from django.conf import settings



class Profile(models.Model):
    pass


















class Country(models.Model):
    name=models.CharField(max_length=20,null=True,blank=True)
    image=models.ImageField()
    slug=models.SlugField(max_length=10)

    def __str__(self):
        return self.name



class CountryDetail(models.Model):
    city=models.CharField(max_length=20,null=True,blank=True)
    phone=models.CharField(max_length=11,null=True,blank=True)
    country=models.ForeignKey(Country,on_delete=models.CASCADE,null=True)
    adress=models.CharField(max_length=50,null=True,blank=True)
    adress2=models.CharField(max_length=50,null=True,blank=True)
    quarter=models.CharField(max_length=50,null=True,blank=True)
    district=models.CharField(max_length=50,null=True,blank=True)
    number=models.CharField(max_length=50,null=True,blank=True)
    post_code=models.CharField(max_length=50,null=True,blank=True)


    def __str__(self):
        return self.country.name


class IncreaseBalance(models.Model):
    card_number=models.IntegerField()




