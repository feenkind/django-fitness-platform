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

    def user_directory_path(self, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/avatar/<filename>
        return f'user_{self.id}/avatar/avatar.{filename.split(".")[1]}'

    avatar = models.ImageField(upload_to=user_directory_path, null=True)

    def __str__(self):
        return f'{self.username} - {self.email}'
