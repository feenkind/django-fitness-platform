import os
from django.db import models
from fitnessplatform import settings
from django.utils.translation import gettext_lazy as _


class Trainer(models.Model):
    class Sports(models.TextChoices):
        YOGA = 'yoga', _('Yoga')
        PERSONAL = 'personal', _('Personal Training')
        TEAM = 'team sports', _('Team Sports')
        DANCE = 'dance', _('Dance')

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    sport = models.CharField(max_length=30, choices=Sports.choices)
    motto = models.CharField(max_length=100)
    about = models.CharField(max_length=500)
    visible = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_fullname(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Upload(models.Model):
    def upload_filename(self):
        filepath = f'user_{self.id}/uploads/'
        fullpath = os.path.join(settings.MEDIA_ROOT, filepath)
        return fullpath

    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='Here goes text')
    url = models.FileField(upload_to=upload_filename, null=True, blank=True, )

    def __str__(self):
        return self.trainer.__str__()


class Location(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    street = models.CharField(max_length=150)
    number = models.CharField(max_length=5)
    zipcode = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    country = models.CharField(max_length=150)

    def __str__(self):
        return self.trainer.__str__()
