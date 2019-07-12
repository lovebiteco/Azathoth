from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = (
            'id', 'reference_id', 'first_name', 'last_name', 'email',
            'date_of_birth', 'gender', 'last_access', 'last_known_position',
            'preferences', 'bio', 'likes', 'nopes', 'blocked', 'matched'
            )

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = User
        fields = UserChangeForm.Meta.fields