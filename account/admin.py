from django.contrib import admin
from .models import CustomUser, TenantProfile
from django.contrib.auth.admin import UserAdmin


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # pass # default
    # add_form = CustomUserCreationForm # used by signup in the app
    # form = CustomUserChangeForm
    list_display = ['username', 'first_name', 'last_name', 'is_active', 'is_superuser']


@admin.register(TenantProfile)
class TenantProfileAdmin(admin.ModelAdmin):
    list_display = ['tenant', 'room_no', 'phone', 'pin']
