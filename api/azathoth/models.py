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
from datetime import timedelta
from django.contrib import admin
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

from lib.fileds import ProtectedForeignKey
from lib.models import BaseModel

class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The email field must not be empty.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

class UserPreferences(BaseModel):
    user = ProtectedForeignKey('User', related_name='preferences', null=False)
    looking_for = models.CharField(max_length=50)
    interested_in = models.CharField(max_length=750)
    similar_match = models.BooleanField(default=False)

class UserBio(BaseModel):
    user = ProtectedForeignKey('User', related_name='bio', null=False)
    description = models.CharField(max_length=500, null=False, blank=True)
    dept_name = models.CharField(max_length=125, null=False, blank=False)
    university_name = models.CharField(max_length=125, null=False, blank=False)
    image_url_1 = models.URLField(null=False, blank=False)
    image_url_2 = models.URLField()
    image_url_3 = models.URLField()
    image_url_4 = models.URLField()
    image_url_5 = models.URLField()

class UserLikes(BaseModel):
    user = ProtectedForeignKey('User', related_name='likes')
    liked_user = models.CharField(max_length=200)
    liked_at = models.DateTimeField()

class UserNopes(BaseModel):
    user = ProtectedForeignKey('User', related_name='nopes')
    noped_user = models.CharField(max_length=200)
    noped_at = models.DateTimeField()

class UserBlocked(BaseModel):
    user = ProtectedForeignKey('User', related_name='blocked')
    blocked_user = models.CharField(max_length=200)
    blocked_at = models.DateTimeField()

class UserMatched(BaseModel):
    user = ProtectedForeignKey()
    matched_user = models.CharField(max_length=200)
    matched_at = models.DateTimeField()


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=True)
    first_name = models.CharField(max_length=250, null=False, blank=False)
    last_name = models.CharField(max_length=250, null=False, blank=False)
    date_of_birth = models.DateTimeField(null=True)
    gender = models.CharField(null=False, blank=False)
    last_access = models.DateTimeField(null=True)
    last_known_position = models.CharField(max_length=250,blank=True)

    preferences = models.ManyToManyField(UserPreferences, related_name='preferences', blank=True)
    bio = models.ManyToManyField(UserBio, related_name='bio', blank=True)
    likes = models.ManyToManyField(UserLikes, related_name='likes')
    nopes = models.ManyToManyField(UserNopes, related_name='nopes')
    blocked = models.ManyToManyField(UserBlocked, related_name='blocked')
    matched = models.ManyToManyField(UserMatched, related_name='matched')

    def __str__(self):
        return self.email

