from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    
    list_display=('first_name','is_staff','is_active')
    list_filter=('first_name','is_staff','is_active')
    fieldsets=(
        (None,{'fields':('first_name','last_name')}),
        ('Permissions',{'fields':('is_staff','is_active')})
    )
    search_fields=('first_name',)
    # ordering=('first_name',)
 
@admin.register(Advisor)
class AdvisorUser(admin.ModelAdmin):
    list_display=['advisor_user','net_balance','total_earning']   

