from rest_framework import serializers, generics
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import settings


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'body', 'topic', 'expiration_time')

class ViewPostSerializer(serializers.ModelSerializer):
    comments= serializers.StringRelatedField(many=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'username', 'expiration_time', 'title', 'body', 'topic', 'likes_count', 'dislikes_count', 'expiration_time', 'is_expired', 'comments')   
        
class CommentCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comment
        fields = ('user', 'username', 'comment', 'post')

class ViewCommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comment
        fields = ('user', 'username', 'comment', 'post')

class LikeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Like
        fields = ('user', 'username', 'liked_post')

class ViewLikeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Like
        fields = ('user', 'username', 'liked_post')

class DislikeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Dislike
        fields = ('user', 'username', 'disliked_post')

class ViewDislikeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Dislike
        fields = ('user', 'username', 'disliked_post')