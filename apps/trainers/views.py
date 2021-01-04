from django.shortcuts import render
from django.template.defaulttags import register
from django.utils.translation import gettext_lazy as _

from apps.trainers.models import *
from apps.trainers.filters import *


# custom template tag to enable multiple level lookup
@register.simple_tag(name='lookup')
def get_item(dictionary, key):
    return dictionary.get(key)


def get_trainer_list(request):
    trainer_filter = TrainerFilter(request.GET, queryset=Trainer.objects.all())
    trainers = list(trainer_filter.qs)
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
        'page_title': _('All Trainers'),
        'trainers': trainers,
        'locations_by_trainerid': locations_by_trainerid,
        'filter': trainer_filter.form,
    }
    return render(request, 'trainers/trainerlist.html', context)


def get_trainer_profile(request, id):
    trainer = Trainer.objects.get(id=id)
    trainername = trainer.get_fullname()
    locations = Location.objects.filter(trainer_id=id)
    context = {
        'page_title': _(f'{trainername}s Profile'),
        'trainer': trainer,
        'trainername': trainername,
        'locations': locations,
    }
    return render(request, 'trainers/trainerprofile.html', context)
