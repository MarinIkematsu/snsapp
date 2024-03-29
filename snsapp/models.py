from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='ログインユーザー名',on_delete=models.CASCADE, null=True)
    title = models.CharField("タイトル", max_length=200)
    image = models.ImageField(upload_to='images', verbose_name='画像', null=True, blank=True)
    content = models.TextField("本文")
    updated_at = models.DateTimeField("更新日", auto_now=True)
    created_at = models.DateTimeField("作成日", auto_now_add=True)

    def __str__(self):
        return self.title




# 機能していません
class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='ログインユーザー名', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, verbose_name='名前')
    icon = models.ImageField(upload_to='icons', verbose_name='アイコン', null=True, blank=True)
    text = models.TextField("自己紹介文")
    updated_at = models.DateTimeField("更新日", auto_now=True)
    created_at = models.DateTimeField("作成日", auto_now_add=True)

    def __str__(self):
        return self.name