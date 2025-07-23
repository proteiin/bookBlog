
from django.forms import Form , ModelForm
from .models import CommentsModel



class commentsForm(ModelForm):
    class Meta:
        model= CommentsModel
        fields = ["comment"]


