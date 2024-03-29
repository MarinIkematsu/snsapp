# snsapp/forms.py
from django import forms
from .models import Post,Profile

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'content']

class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image','content']




# 使うかわからないプロフィール
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'icon', 'text']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'icon', 'text']