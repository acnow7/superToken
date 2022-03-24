from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.blog import BlogSerializer
from ..models.blog import Blog
from rest_framework import status
from django.shortcuts import get_object_or_404


class BlogsView(APIView):
    def get(self, request):
         # filter for mangos with our user id
        blogs = Blog.objects.filter(author=request.user.id)
        data = BlogSerializer(blogs, many = True).data
        return Response(data)

    def post(self, request):
        request.data['author'] = request.user.id
        blog = BlogSerializer(data=request.data)
        if blog.is_valid():
            blog.save()
            return Response(blog.data, status=status.HTTP_201_CREATED)
        else:
            return Response(blog.errors, status=status.HTTP_400_BAD_REQUEST)