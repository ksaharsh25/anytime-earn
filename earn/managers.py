from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self,  first_name, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not first_name:
            raise ValueError("The first name must be set")
        user=self.model(first_name=first_name,**extra_fields)
        # last_name = last_name.capitalize()
       
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,first_name, password, **extra_fields):
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
        return self.create_user(first_name, password, **extra_fields)
