from django.db import models
from django.conf import settings
from post.models import PostModel
from accounts.models import CustomUser
# Create your models here.

class CommentsModel(models.Model):
    comment = models.TextField(max_length=200)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE,related_name='comments')
    time = models.DateTimeField(auto_now=False, auto_now_add=True)

