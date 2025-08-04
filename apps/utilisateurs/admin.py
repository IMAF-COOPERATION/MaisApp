from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('Informations personnelles', {'fields': ('telephone', 'photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
