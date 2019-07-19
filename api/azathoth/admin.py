from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, UserLocation

from django.contrib.gis.admin import OSMGeoAdmin

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = [
            'id', 'reference_id', 'username', 'email', 'is_staff', 'is_active', 'is_superuser', 'first_name', 'last_name',
            'date_of_birth', 'gender', 'last_access',
        ]

admin.site.register(User, CustomUserAdmin)


@admin.register(UserLocation)
class LocationAdmin(OSMGeoAdmin):
    list_display = [
        'reference_id', 'location'
    ]

# Register your models here.
