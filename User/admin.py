from django.contrib import admin

# Register your models here.
from User.models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import *
# Register your models here.

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Extra fields',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'phone_no',
                    'address',
                    'role',
                    'route_name',
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            'Add new user',
            {
                'classes': ('wide',),
                'fields': (
                    'username',
                    'password1',
                    'password2', 
                    'first_name', 
                    'last_name', 
                    'role', 
                    'phone_no', 
                    'route_name',
                    'assigned_counter', 
                    'address' 
                ),
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)