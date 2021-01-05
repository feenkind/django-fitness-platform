from django.shortcuts import render
from django.template.defaulttags import register

from apps.trainers.models import *


# custom template tag to enable multiple level lookup
@register.simple_tag(name='lookup')
def get_item(dictionary, key):
    return dictionary.get(key)


def get_trainer_list(request):
    trainers = list(Trainer.objects.all().order_by('user'))
    locations = Location.objects.all()
    locations_by_trainerid = {}
    for location in locations:
        # check if trainer already has an associated location in dictionary
        location_list = locations_by_trainerid.get(location.trainer_id)
        if not location_list:
            # trainers can have more than one address, therefore we have to use a list of locations
            location_list = list()
        location_list.append(location)
        # assign complete location_list to corresponding trainer_id key
        locations_by_trainerid[location.trainer_id] = location_list
    context = {
        'page_title': 'All Trainers',
        'trainers': trainers,
        'locations_by_trainerid': locations_by_trainerid,
    }
    return render(request, 'trainers/trainerlist.html', context)


def get_trainer_profile(request, id):
    trainer = Trainer.objects.get(id=id)
    trainername = trainer.get_fullname()
    locations = Location.objects.filter(trainer_id=id)
    context = {
        'page_title': f'{trainername}s Profile',
        'trainer': trainer,
        'trainername': trainername,
        'locations': locations,
    }
    return render(request, 'trainers/trainerprofile.html', context)
