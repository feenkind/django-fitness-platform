# Generated by Django 3.1.4 on 2021-01-05 14:35

import apps.users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(null=True, upload_to=apps.users.models.User.user_directory_path),
        ),
    ]
