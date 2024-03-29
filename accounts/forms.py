from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


#class SignUpForm(UserCreationForm):
    #class Meta:
        #model = CustomUser
        #fields = ('username', 'email')
        # fields = ['username', 'email', 'password']
        # labels = {
        #     'username': 'ユーザー名',
        #     'email': 'メールアドレス',
        #     'password': 'パスワード',
        # }
        # widgets = {
        #     'password': forms.PasswordInput(),
        # }


class SignInForm(forms.Form):
    username = forms.CharField(label='ユーザー名')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput)