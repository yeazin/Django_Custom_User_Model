from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import  New_User_Custom
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea, TextInput
# Register your models here.


class Custom_admin(UserAdmin):
    model = New_User_Custom
    list_display = ['user_name','email','first_name','last_name', 'is_admin','is_superuser','is_staff','is_active']
    list_filter  = ['user_name','email','first_name','last_name']
    ordering = ['-start_date']
    search_fields = ['user_name','email','first_name','last_name']

    fieldsets = (
        (None, {'fields' : ('email','user_name','first_name','last_name')}),
        ('Permission', {'fields':('is_admin','is_superuser','is_staff','is_active')}),
        ('Personal',{'fields':('about','start_date')} )
    )
    formfield_overrides = {
        New_User_Custom.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }
    add_fieldsets = (
        (None,{'classes':('wide'),
        'fields':('user_name','email','first_name','last_name','password1','password2','is_staff','is_admin','is_superuser','is_active')}),
    )
admin.site.register(New_User_Custom,Custom_admin)
