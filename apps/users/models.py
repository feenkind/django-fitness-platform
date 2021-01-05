from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
import os


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
        # file will be uploaded to MEDIA_ROOT/user_<id>/avatar/avatar.<extension>
        name = f'avatar.{filename.split(".")[1]}'
        path = f'user_{self.id}/avatar/'
        fullpath = os.path.join(settings.MEDIA_ROOT, path)
        if os.path.exists(fullpath):
            for filename in os.listdir(fullpath):
                # remove any exiting avatar file
                if filename.startswith('avatar'):
                    os.remove(f'{fullpath}/{filename}')

        return f'{path}/{name}'

    avatar = models.ImageField(
        upload_to=user_directory_path,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.username} - {self.email}'
