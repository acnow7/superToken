from rest_framework import serializers
from ..models.blog import Blog
from .user import UserSerializer

class BlogSerializer(serializers.ModelSerializer):
    author = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Blog
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'author')

class UpdateBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'updated_at', 'author')

class BlogSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'content', 'created_at', 'author')