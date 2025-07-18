from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username","nickname","name")
        widget = {

        }

# //class CustomUser(AbstractUser):
#     nickname = models.CharField(max_length=30, unique=True, null=True)
#     name = models.CharField(max_length=10, unique=False, null=True)
#     books = models.CharField(max_length=10, unique=True, null=False)
#     reviews = models.CharField(max_length=10, unique=True, null=False)
    
