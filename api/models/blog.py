from django.db import models
from django.contrib.auth import get_user_model

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=400)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    