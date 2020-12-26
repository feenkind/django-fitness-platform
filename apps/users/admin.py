from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.


class UsersAdmin(UserAdmin):
    model = User


admin.site.register(User, UsersAdmin)
