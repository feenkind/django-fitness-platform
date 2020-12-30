from django.db import models
from fitnessplatform import settings


# class Sports(models.TextChoices):
#     YOGA = 'yoga',

class Trainer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sport = models.CharField(max_length=30)
    motto = models.CharField(max_length=100)
    about = models.CharField(max_length=500)

    def __str__(self):
        return self.user.username

class Upload(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    url = models.URLField(max_length=30)

    def __str__(self):
        return f'{self.trainer.__str__()} ({self.url})'

class Location(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    street = models.CharField(max_length=40)
    number = models.CharField(max_length=5)
    zipcode = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.trainer.__str__()