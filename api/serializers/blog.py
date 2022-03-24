from rest_framework import serializers
from ..models.blog import Blog
from .user import UserSerializer
from .comments import CommentSerializer1

class BlogSerializer(serializers.ModelSerializer):
    author = UserSerializer(many=False, read_only=True)
    comments = CommentSerializer1(many=True, read_only=True)
    class Meta:
        model = Blog
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'author', 'comments')

class UpdateBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'content', 'title', 'updated_at', 'author')

class BlogSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'content', 'created_at', 'author')