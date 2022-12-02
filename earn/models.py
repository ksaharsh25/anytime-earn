from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.db.models.signals import post_save
# Create your models here.
class CustomUser(AbstractUser):
    username=None
    first_name=models.CharField(_('first name'),max_length=50,blank=False,unique=True)
    middle_name=models.CharField(max_length=50,blank=True)
    last_name=models.CharField(max_length=50,blank=False)
    email=models.EmailField(max_length=50,blank=False)
    mobile=models.IntegerField(max_length=10,unique=True,null=True) 
   

    USERNAME_FIELD = 'first_name'
    REQUIRED_FIELDS = [] 

    objects = CustomUserManager() 

    def __str__(self):
        if self.middle_name:
            return f"{self.first_name} {self.middle_name} {self.last_name}"

        else:
            return f"{self.first_name} {self.last_name}"

class Advisor(models.Model):
    advisor_user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True)
    net_balance=models.DecimalField(max_digits=5,decimal_places=2,validators=[MinValueValidator(Decimal('0.00 '))],null=True)    
    total_earning =models.DecimalField(max_digits=5,decimal_places=2,validators=[MinValueValidator(Decimal('0.00 '))],null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


def create_wallet(sender,instance,created,**kwargs):
    if created:
        Advisor.objects.create(advisor_user=instance)
        instance.save()
post_save.connect(create_wallet,sender=CustomUser)        
