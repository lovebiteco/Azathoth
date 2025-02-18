from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'date_of_birth', 'gender', 'last_access',
             )

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = User
        fields = UserChangeForm.Meta.fields