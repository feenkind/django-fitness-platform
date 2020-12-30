from django.db import models
from fitnessplatform import settings

class Trainer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sport = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    motto = models.CharField(max_length=100)
    about = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username

class Upload(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    url = models.URLField(max_length=30)

    def __str__(self):
        return f'{self.trainer.__str__()} ({self.url})'

