from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager




class User(AbstractUser):
    first_name = None
    last_name = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
















# class CustomUserManager(BaseUserManager):
#     """
#     Custom user model manager where email is the unique identifiers
#     for authentication instead of usernames.
#     """
#     def create_user(self, email, password, **extra_fields):
#         """
#         Create and save a User with the given email and password.
#         """
#         if not email:
#             raise ValueError(_('The Email must be set'))
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, email, password, **extra_fields):
#         """
#         Create and save a SuperUser with the given email and password.
#         """
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError(_('Superuser must have is_staff=True.'))
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError(_('Superuser must have is_superuser=True.'))
#         return self.create_user(email, password, **extra_fields)

# class CustomUserManager(BaseUserManager):
#     """
#     Custom user model manager where email is the unique identifiers
#     for authentication instead of usernames.
#     """
#     def create_user(self, email, password, **extra_fields):
#         """
#         Create and save a User with the given email and password.
#         """
#         if not email:
#             raise ValueError(_('The Email must be set'))
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, email, password, **extra_fields):
#         """
#         Create and save a SuperUser with the given email and password.
#         """
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError(_('Superuser must have is_staff=True.'))
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError(_('Superuser must have is_superuser=True.'))
#         return self.create_user(email, password, **extra_fields)


# class User(AbstractUser):

#     GENDER_CHOICES=(
#         ('Qadın','Qadın'),
#         ('Kişi','Kişi')
#     )

#     DAY_CHOICES=(
#         ('1','1'),
#         ('2','2')
#     )

#     MONTH_CHOICES=(
#         ('Yanvar','Yanvar'),
#         ('Fevral','Fevral')
#     )

#     YEAR_CHOICES=(
#         ('2003','2003'),
#         ('2004','2004')
#     )



#     first_name = models.CharField(max_length=50,null=True)
#     last_name = models.CharField(max_length=50,null=True)
#     gender=models.CharField(max_length=50,choices=GENDER_CHOICES)
#     day=models.CharField(max_length=50,choices=DAY_CHOICES)
#     month=models.CharField(max_length=50,choices=MONTH_CHOICES)
#     year=models.CharField(max_length=50,choices=YEAR_CHOICES)
#     network_type=models.CharField()
#     user_number=models.IntegerField()
#     email = models.EmailField(_('email address'), unique=True)


#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name','last_name','gender','day','month','year','network_type','email']

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email
