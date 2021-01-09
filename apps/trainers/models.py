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
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    url = models.URLField(max_length=30)

    def __str__(self):
        return f'{self.trainer.__str__()} ({self.url})'


class Location(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    street = models.CharField(max_length=40)
    number = models.CharField(max_length=5)
    zipcode = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.trainer.__str__()