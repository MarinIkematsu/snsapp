from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

admin.site.register(CustomUser)


"""
class CustomUserAdmin(UserAdmin):
    add_form = SignUpForm
    model = CustomUser
"""