from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from allauth.socialaccount.models import SocialToken, SocialAccount, SocialApp
from allauth.account.models import EmailAddress
from .models import User


class UserAdmin(admin.ModelAdmin):
    exclude = ['last_login', 'groups', 'user_permissions', 'password']


admin.site.register(User, UserAdmin)

# hide unneeded allauth model
admin.site.unregister(EmailAddress)
