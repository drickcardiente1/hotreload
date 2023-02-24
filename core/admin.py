from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class Users(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'first_name', 'last_name', 'last_login','type','otp')}),
        ('Permissions', {'fields': (
            'is_active', 
            'is_staff', 
            'is_admin',
            'is_client',
            'groups', 
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('username', 'email', 'password1', 'password2','type','otp')
            }
        ),
    )

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_admin', 'last_login','type')
    list_filter = ('is_staff', 'is_admin', 'is_active', 'groups')
    search_fields = ('email', 'username',)
    ordering = ('email', 'username',)
    filter_horizontal = ('groups', 'user_permissions',)


class Usersadmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'first_name', 'last_name', 'last_login','type','otp')}),
        ('Permissions', {'fields': (
            'is_active', 
            'is_staff', 
            'is_admin',
        )}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_admin', 'last_login','type')
    search_fields = ('email', 'username',)
    ordering = ('email', 'username',)
    def has_add_permission(self, request, obj=None):
        return False


class Usersclient(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'first_name', 'last_name', 'last_login','type','otp')}),
        ('Permissions', {'fields': (
            'is_active', 
            'is_client',
        )}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_admin', 'last_login','type')
    search_fields = ('email', 'username',)
    ordering = ('email', 'username',)
    def has_add_permission(self, request, obj=None):
        return False
        


admin.site.register(account,Users)
admin.site.register(administrator,Usersadmin)
admin.site.register(client,Usersclient)
