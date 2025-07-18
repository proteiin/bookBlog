from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=30, unique=True, null=True)
    name = models.CharField(max_length=10, unique=False, null=True)
    # books = models.CharField(max_length=10, unique=False, null=False)
    # reviews = models.CharField(max_length=10, unique=False, null=False)
    
