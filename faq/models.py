from django.db import models

# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=50,unique=True,null=True)


    class Meta:
        verbose_name_plural='Kateqoriyalar'
    

    def __str__(self):
        return self.name



class Question(models.Model):
    question=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='questions',null=True)


    class Meta:
        verbose_name_plural='Suallar'

    def __str__(self):
        return self.question

