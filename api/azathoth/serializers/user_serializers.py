from rest_framework import serializers
from rest_framework.response import Response
from azathoth import models

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = [
            'id', 'reference_id', 'first_name', 'last_name', 'email',
            'is_staff', 'is_active', 'is_superuser',
            'date_of_birth', 'gender', 'last_access', 'last_known_position',
            'likes', 'nopes', 'blocked', 'matched'
        ]

class UserLikesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserLikes
        fields = {
            'id', 'reference_id', 'user', 'liked_user', 'liked_at'
        }

class UserNopesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserNopes
        fields = {
            'id', 'reference_id', 'user', 'noped_user', 'noped_at'
        }

class UserBlockedSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserBlocked
        fields = {
            'id', 'reference_id', 'user', 'blocked_user', 'blocked_at'
        }

class UserMatchedSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserMatched
        fields = {
            'id', 'reference_id', 'user', 'matched_user', 'matched_at'
        }

