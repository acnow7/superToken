from rest_framework import serializers
from ..models.blog import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'content', 'created_at','updated_at', 'author')

class UpdateBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'updated_at', 'author')