from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from django.db.models.fields import BLANK_CHOICE_DASH, EmailField
#from django.db.models.fields import DateField,EmailField

###############       creating custom user model for django projects       #####


#for base user models
#check the official docs https://docs.djangoproject.com/en/3.1/topics/auth/customizing/

#for creating base model

class Custom_Account_Manager(BaseUserManager):

    def create_superuser(self,email,user_name,first_name,password, **other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active',True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(' User must be staff')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('User must be superuser')
        
        return self.create_user(email,user_name,first_name,password, **other_fields)

        
    def create_user(self,email, user_name, first_name, password, **other_fields):
        email       =   self.normalize_email(email)
        user        =   self.model(email=email, user_name=user_name, first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


#for creating new user

class New_User_Custom(AbstractBaseUser,PermissionsMixin):
    email           =   models.EmailField(verbose_name='Email Address', unique=True,max_length=200)
    user_name       =   models.CharField(verbose_name='User Name', unique=True, max_length=100)
    first_name      =   models.CharField(verbose_name='First Name', blank=True,max_length=100)
    last_name       =   models.CharField(verbose_name='Last Name', max_length=200, blank=True)
    about           =   models.TextField(max_length=500, blank=True)
    start_date      =   models.DateTimeField(default=timezone.now)
    is_admin        =   models.BooleanField(default=False)
    is_active       =   models.BooleanField(default=False)
    is_staff        =   models.BooleanField(default=False)
    is_superuser    =   models.BooleanField(default=False)

    objects         =   Custom_Account_Manager()

    USERNAME_FIELD  =   'email'
    REQUIRED_FIELDS =   ['user_name','first_name']

    class Meta:
        verbose_name_plural = 'New User Account'
        

    def __str___(self):
        return self.user_name + "," + self.email
