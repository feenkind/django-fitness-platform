# Generated by Django 3.1.4 on 2021-01-16 14:59

import apps.trainers.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainers', '0003_auto_20210110_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='title',
            field=models.CharField(default='Filename', max_length=100),
        ),
        migrations.AlterField(
            model_name='upload',
            name='url',
            field=models.FileField(blank=True, null=True, upload_to=apps.trainers.models.Upload.upload_filename),
        ),
    ]
