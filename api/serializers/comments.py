from rest_framework import serializers
from ..models.comments import Comment
from .user import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(many=False, read_only=True)
    # blog = BlogSerializer1()(many=False, read_only=True)
    class Meta:
        model = Comment
        fields = ('id', 'content', 'created_at', 'updated_at', 'author', 'blog')

class UpdatedCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'updated_at', 'author')

class CommentSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'created_at', 'updated_at', 'author', 'blog')