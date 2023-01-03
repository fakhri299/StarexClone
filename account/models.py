from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin



class UserManager(BaseUserManager):
    def create_user(self,email,password,**extra_kwargs):
        email=self.normalize_email(email)

        user = self.model(email=email,**extra_kwargs)

        user.set_password(password)
        
        user.save()
        return user


    def create_superuser(self,email, password, **extra_fields):
        
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


from.choices import( 
DAY_CHOICES,MONTH_CHOICES,
GENDER_CHOCIES,DISTRICT_CHOICES,ID_CARD_SERIA_CHOICES)






class CustomUser(AbstractUser,PermissionsMixin):
    username=None
    first_name=models.CharField(max_length=50,null=True,blank=True)
    last_name=models.CharField(max_length=50,null=True,blank=True)
    gender=models.CharField(max_length=50,choices=GENDER_CHOCIES,null=True,blank=True)
    day=models.CharField(max_length=10,choices=DAY_CHOICES,null=True,blank=True)
    month=models.CharField(max_length=20,choices=MONTH_CHOICES,null=True,blank=True)
    year= models.CharField(max_length=4,null=True,blank=True)
    telephon=models.CharField(max_length=50,null=True)
    email=models.EmailField(max_length=50,unique=True)
    district=models.CharField(max_length=50,choices=DISTRICT_CHOICES)
    id_card_seria=models.CharField(max_length=20,choices=ID_CARD_SERIA_CHOICES,default='AZE')
    fin_code=models.CharField( max_length=7,unique=True,null=True)
    id_card_number=models.CharField(max_length=7,null=True,unique=True)
    adress=models.CharField(max_length=50,null=True,blank=True)
    filial=models.CharField(max_length=50)
    password_again=models.CharField(max_length=8,null=True,blank=True)
    promocode=models.CharField(max_length=10,null=True,blank=True)
    

    objects=UserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    def __str__(self):
        return f'{self.email}'
 

    




