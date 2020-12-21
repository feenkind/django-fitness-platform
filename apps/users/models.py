from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Roles(models.TextChoices):
    ADMIN = 'admin', _('Admin')
    TRAINER = 'trainer', _('Trainer')
    USER = 'user', _('User')


class User(AbstractUser):
    role = models.CharField(
        max_length=150,
        choices=Roles.choices,
        default=Roles.USER,
    )
