from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.blog import BlogSerializer, UpdateBlogSerializer, BlogSerializer1
from ..models.blog import Blog
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied

class BlogsView(APIView):
    def get(self, request):
         # filter for mangos with our user id
        # blogs = Blog.objects.filter(author=request.user.id)
        blogs = Blog.objects.all()
        data = BlogSerializer(blogs, many = True).data
        return Response(data)

    def post(self, request):
        request.data['author'] = request.user.id
        blog = BlogSerializer1(data=request.data)
        if blog.is_valid():
            blog.save()
            return Response(blog.data, status=status.HTTP_201_CREATED)
        else:
            return Response(blog.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogView(APIView):
    def get(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        data = BlogSerializer(blog).data
        return Response(data)

    def put(self, request, pk):
        request.data['author'] = request.user.id
        blog = get_object_or_404(Blog, pk=pk)
        if request.user != blog.author:
            raise PermissionDenied('Unauthorized user')
        updated_blog = UpdateBlogSerializer(blog, data=request.data, partial=True)
        if updated_blog.is_valid():
            updated_blog.save()
            return Response(updated_blog.data)
        else:
            return Response(updated_blog.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        if request.user != blog.author:
            raise PermissionDenied('Unauthorized user')
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MyBlogsView(APIView):
    def get(self, request):
         # filter for mangos with our user id
        blogs = Blog.objects.filter(author=request.user.id)
        data = BlogSerializer(blogs, many = True).data
        return Response(data)