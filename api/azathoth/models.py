#   _                   ____  _ _       
#  | |    _____   _____| __ )(_) |_ ___ 
#  | |   / _ \ \ / / _ \  _ \| | __/ _ \
#  | |__| (_) \ V /  __/ |_) | | ||  __/
#  |_____\___/ \_/ \___|____/|_|\__\___|
#                                       
#  
#  
#                       Leonardo Corsaro
#  Nicola Gigante <nicolagigante@outlook.com>
#                                       
#  


from django.db import models
from django.contrib.gis.db import models as models_gis
from datetime import timedelta
from django.contrib import admin
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

from lib.fields import ProtectedForeignKey
from lib.models import BaseModel

import uuid

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError('The email field must not be empty.')
        if not username:
            raise ValueError('This field must not be empty.')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username,**extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError('The email field must not be empty.')
        if not username:
            raise ValueError('This field must not be empty.') 
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.is_first_login = False
        user.set_password(password)
        user.save()
        return user



class UserBlocked(BaseModel):
    blocked_user = models.CharField(max_length=200)
    blocked_at = models.DateTimeField()

class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=125)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_first_login = models.BooleanField(default=True)

    email = models.EmailField(unique=True, null=True)
    first_name = models.CharField(max_length=250, null=False, blank=False)
    last_name = models.CharField(max_length=250, null=False, blank=False)
    date_of_birth = models.DateTimeField(null=True)
    gender = models.CharField(max_length=30, null=False, blank=False)
    last_access = models.DateTimeField(null=True)

    looking_for = models.CharField(max_length=50)
    interested_in = models.CharField(max_length=750)
    similar_match = models.BooleanField(default=False)

    description = models.CharField(max_length=500, null=False, blank=True)
    dept_name = models.CharField(max_length=125, null=False, blank=False, default="Engineering")
    university_name = models.CharField(max_length=125, null=False, blank=False, default="UCL")
    image_url_1 = models.URLField(blank=True)
    image_url_2 = models.URLField(blank=True)
    image_url_3 = models.URLField(blank=True)
    image_url_4 = models.URLField(blank=True)
    image_url_5 = models.URLField(blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email

class UserLikes(BaseModel):
    liked_user = models.CharField(max_length=200)
    liked_at = models.DateTimeField()
    users = models.ManyToManyField(User)

class UserNopes(BaseModel):
    noped_user = models.CharField(max_length=200)
    noped_at = models.DateTimeField()
    users = models.ManyToManyField(User)

class UserMatched(BaseModel):
    matched_user = models.CharField(max_length=200)
    matched_at = models.DateTimeField()
    users = models.ManyToManyField(User)

class UserLocation(models_gis.Model):
    users = models_gis.ManyToManyField(User)
    location = models_gis.PointField()
    created_at = models_gis.DateTimeField(editable=False, auto_now_add=True)
    reference_id = models_gis.UUIDField(default=uuid.uuid4, editable=False, unique=True)



