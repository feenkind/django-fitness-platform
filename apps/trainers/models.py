from django.db import models

# Create your models here.

class Trainer(models.Model):
    # id
    # userid = models.ForeignKey(User, on_delete=models.CASCADE)
    desc = models.CharField(max_length=200)
    sport = models.CharField(max_length=20)
    motto = models.CharField(max_length=40)

class Uploads(models.Model):
    # id
    trainerid = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    url = models.CharField(max_length=30)
