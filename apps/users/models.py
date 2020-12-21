from django.contrib.auth.models import AbstractUser
from django.db.models import CharField


class User(AbstractUser):
    role_choices = [
        ('trainer', 'Trainer'),
        ('user', 'User'),
        ('admin', 'Admin'),
    ]

    role = CharField(
        max_length=150,
        choices=role_choices,
        default='user',
    )
