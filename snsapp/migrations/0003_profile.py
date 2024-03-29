# Generated by Django 4.2.6 on 2024-03-20 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snsapp', '0002_alter_post_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='icons', verbose_name='アイコン')),
                ('text', models.TextField(verbose_name='自己紹介文')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]