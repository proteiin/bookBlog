from django.db import models
from django import forms
from .models import PostModel

class myPostModelForm(forms.ModelForm):
    class Meta:
        model= PostModel
        fields = ['bookName','title','review']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '제목을 입력하세요'
            }),
            'review': forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'리뷰를 입력하세요',
                'rows': 7
            })

        }