from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
        )