from django.db import models
from django.contrib.auth import get_user_model
from .blog import Blog

class Comment(models.Model):
    content = models.CharField(max_length=100)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    blog = models.ForeignKey(
        Blog, 
        on_delete=models.CASCADE,
        related_name= 'comments'
    )
       
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
def __str__(self):
    # This must return a string
    return f"Comment: '{self.content}' by {self.author} created on {self.created_at}."