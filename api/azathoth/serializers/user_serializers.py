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
            'preferences', 'bio', 'likes', 'nopes', 'blocked', 'matched'
        ]

class UserBioSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserBio
        fields = {
            'id', 'reference_id', 'user', 'description', 'dept_name',
            'university_name', 'image_url_1', 'image_url_2', 'image_url_3',
            'image_url_4', 'image_url_5'
        }

class UserPreferencesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserPreferences
        fields = {
            'id', 'reference_id', 'user', 'looking_for', 'interested_in',
            'similar_match'
        }

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

