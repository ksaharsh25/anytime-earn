from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Admin)
class Adminadmin(admin.ModelAdmin):
    list_display=['first_name','last_name']