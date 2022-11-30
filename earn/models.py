from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin


# Create your models here.
class CustomUser(AbstractUser):
    username=None
    first_name=models.CharField(_('first name'),max_length=50,blank=False,unique=True)
    middle_name=models.CharField(max_length=50,blank=True)
    last_name=models.CharField(max_length=50,blank=False)
    email=models.EmailField(max_length=50,blank=False)
     
   

    USERNAME_FIELD = 'first_name'
    REQUIRED_FIELDS = [] 

    objects = CustomUserManager() 

    def __str__(self):
        if self.middle_name:
            return f"{self.first_name} {self.middle_name} {self.last_name}"

        else:
            return f"{self.first_name} {self.last_name}"

    