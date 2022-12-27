from django.db import models



class Country(models.Model):
    name=models.CharField(max_length=20)
    slug=models.SlugField(max_length=50,unique=True,null=True)


    class Meta:
        verbose_name_plural='Ölkələr'

    def __str__(self):
        return self.name

class Shop(models.Model):
    shop_link=models.URLField(max_length=100,unique=True,blank=True)
    image=models.ImageField(upload_to="media/shop_photos/%Y/%m/%d/", null=True, blank=True)
    country=models.ForeignKey(Country,on_delete=models.CASCADE,null=True)
    

    class Meta:
        verbose_name_plural='Mağazalar'

    def __str__(self):
        return self.shop_link
