from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Post, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password',
        )

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'body',
            'author'
        )

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'post_id',
            'body',
            'author'
        )