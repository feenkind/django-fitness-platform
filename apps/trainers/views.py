from django.shortcuts import render

from apps.trainers.models import *


def get_trainer_list(request):
    trainers = Trainer.objects.all().order_by('user')
    return render(request, 'trainers/trainerlist.html', {
        'page_title': 'All Trainers',
        'trainers': trainers
    })


def get_trainer_profile(request):
    return render(request, 'trainers/trainerprofile.html')
