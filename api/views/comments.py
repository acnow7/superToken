from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.comments import CommentSerializer1
from ..models.comments import Comment
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied
from ..models.blog import Blog
class CommentView(APIView):
    # def get(self, request):
    #      # filter for mangos with our user id
    #     # blogs = Blog.objects.filter(author=request.user.id)
    #     blogs = Blog.objects.all()
    #     data = BlogSerializer(blogs, many = True).data
    #     return Response(data)

    def post(self, request, pk):
        request.data['author'] = request.user.id
        blog = get_object_or_404(Blog, pk=pk)
        request.data['blog'] = blog.id
        comment = CommentSerializer1(data=request.data)
        if comment.is_valid():
            comment.save()
            return Response(comment.data, status=status.HTTP_201_CREATED)
        else:
            return Response(comment.errors, status=status.HTTP_400_BAD_REQUEST)
