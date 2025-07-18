from django.db import models
from django.conf import settings
from django import forms

class PostModel(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    bookName = models.CharField(max_length=20, blank=True)
    time = models.DateTimeField(blank=True,null=True)
    title = models.CharField(max_length=20, blank=True)
    review = models.CharField(max_length=800, blank=True)