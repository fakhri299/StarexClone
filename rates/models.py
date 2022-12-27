from django.db import models






class Tarif(models.Model):
    rangeweight=models.CharField(max_length=100,null=True)
    price=models.CharField(max_length=50)
    countryandtype=models.CharField(max_length=100,null=True)

    class Meta:
        verbose_name_plural='Tariflər'



    def __str__(self):
        return f' {self.countryandtype}'


class RateType(models.Model):
    name=models.CharField(max_length=50,null=True)
    slug=models.SlugField(max_length=50,null=True)
    tarif=models.ManyToManyField(Tarif)

    class Meta:
        verbose_name_plural='Tariflərin Növü'
    

    
    def __str__(self):
        return f'{self.name}'



class Country(models.Model):
    name=models.CharField(max_length=50,null=True)
    slug=models.SlugField(max_length=50,null=True)
    cargo_type=models.ManyToManyField(RateType,blank=True)


    class Meta:
        verbose_name_plural='Ölkələr'

    def __str__(self):
        return f'{self.name}'


