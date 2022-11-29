from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

from django.utils.translation import gettext_lazy as _
class CustomUserManager(BaseUserManager):
    def create_user(self,  first_name, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError("The email must be set")
        first_name = first_name.capitalize()
        # last_name = last_name.capitalize()
        email = self.normalize_email(email)

        user = self.model(
            first_name=first_name, email=email, **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,first_name, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)


        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email,first_name, password, **extra_fields)


# Create your models here.
class Admin(AbstractUser):
    first_name=models.CharField(max_length=50,blank=False,unique=True,null=True)
    middle_name=models.CharField(max_length=50,blank=True)
    last_name=models.CharField(max_length=50,blank=False)
    email=models.EmailField(max_length=50,blank=False)
    password=models.CharField(max_length=50,blank=False)
    is_staff = models.BooleanField(null=True)
    is_active = models.BooleanField(null=True)

    USERNAME_FIELD = 'first_name'
    REQUIRED_FIELDS = ['email'] 

    objects = CustomUserManager() 

    def __str__(self):
        if self.middle_name:
            return f"{self.first_name} {self.middle_name} {self.last_name}"

        else:
            return f"{self.first_name} {self.last_name}"

    def has_perm(self, perm, obj=None):
        return self.is_staff

    # this methods are require to login super user from admin panel
    def has_module_perms(self, app_label):
        return self.is_staff      