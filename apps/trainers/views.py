from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.defaulttags import register
from django.urls import reverse_lazy
from apps.trainers.models import *
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from apps.trainers.forms import TrainerSettings
from apps.users.models import Roles


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


def get_trainer_profile(request, id=None):
    try:
        trainer = (
            Trainer.objects.get(id=id)
            if id
            else Trainer.objects.get(user_id=request.user.id)
        )
        trainername = trainer.get_fullname()
        locations = Location.objects.filter(trainer_id=id)
        context = {
            'page_title': f'{trainername}s Profile',
            'trainer': trainer,
            'trainername': trainername,
            'locations': locations,
        }
    except Trainer.DoesNotExist:
        user = request.user
        if user.role != Roles.TRAINER:
            return
        else:
            context = {'page_title': 'Trainerprofile does not exist.'}

    return render(request, 'trainers/trainerprofile.html', context)


def edit_trainer_profile(request):
    user = request.user
    if user.role != Roles.TRAINER:
        return
    try:
        trainer = Trainer.objects.get(user_id=user.id)
    except:
        trainer = Trainer()
    if request.method == 'POST':
        form = TrainerSettings(request.POST, instance=trainer)
        if form.is_valid():
            trainer.user_id = user.id
            form.save()
            messages.success(request, _('Profile saved'))
            return HttpResponseRedirect(reverse_lazy('trainer_profile'))
        else:
            messages.error(request, _('We had problems saving your changes.'))
    else:
        form = TrainerSettings(instance=trainer)
    context = {
        'page_title': f'Edit trainer profile',
        'form': form,
    }
    return render(request, 'trainers/trainerprofile_edit.html', context)
