from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.template.defaulttags import register
from django.urls import reverse_lazy
from apps.trainers.models import *
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from apps.trainers.forms import TrainerSettings, LocationSettings
from apps.users.models import Roles
from apps.trainers.filters import *


# custom template tag to enable multiple level lookup


@register.simple_tag(name='lookup')
def get_item(dictionary, key):
    return dictionary.get(key)


def get_trainer_list(request):
    trainer_filter = TrainerFilter(request.GET, queryset=Trainer.objects.all())
    trainers = list(trainer_filter.qs.filter(visible=True))
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
        'result_count': trainers.__len__,
    }
    return render(request, 'trainers/trainerlist.html', context)


def get_trainer_profile(request, id=None):
    show_edit = False
    show_create = False
    try:
        trainer = (
            Trainer.objects.get(id=id)
            if id
            else Trainer.objects.get(user_id=request.user.id)
        )
        if trainer.user_id == request.user.id:
            show_edit = True
        trainername = trainer.get_fullname()
        locations = Location.objects.filter(trainer_id=trainer.id)
        marked_favorite = trainer.is_flagged(request.user)
        user_can_favorite = (
            hasattr(request.user, 'role') and request.user.role == Roles.USER
        )

        context = {
            'page_title': f'{trainername}\'s profile',
            'trainer': trainer,
            'trainername': trainername,
            'locations': locations,
            'show_edit': show_edit,
            'show_create': show_create,
            'is_visible': trainer.visible,
            'marked_favorite': marked_favorite,
            'user_can_favorite': user_can_favorite,
        }
    except Trainer.DoesNotExist:
        if (
            not id
            and hasattr(request.user, 'role')
            and request.user.role == Roles.TRAINER
        ):
            show_create = True

        context = {
            'page_title': 'Trainerprofile does not exist',
            'show_edit': show_edit,
            'show_create': show_create,
        }

    return render(request, 'trainers/trainerprofile.html', context)


def edit_trainer_profile(request):
    user = request.user
    if not user.is_authenticated or user.role != Roles.TRAINER:
        return render(request, '404.html')
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
        'page_title': 'Edit trainer profile',
        'form': form,
        'is_visible': trainer.visible,
    }
    return render(request, 'trainers/trainerprofile_edit.html', context)


def edit_trainer_locations(request, id=None, action=None):
    user = request.user
    try:
        trainer = Trainer.objects.get(user_id=user.id)
        locations = Location.objects.filter(trainer_id=trainer.id)
        location = None
        create = True if action == 'new' else False
        if id:
            location = locations.get(id=id)
        elif create:
            location = Location()
            location.trainer_id = trainer.id
        if request.method == 'POST':
            form = LocationSettings(request.POST, instance=location)
            if form.is_valid():
                location.trainer = trainer
                form.save()
                messages.success(request, _('Location saved'))
                return HttpResponseRedirect(
                    reverse_lazy('trainer_profile_locations')
                )
        else:
            form = LocationSettings(instance=location)
        context = {
            'page_title': 'Edit your locations',
            'locations': locations,
            'location': location,
            'form': form,
            'action': action,
        }

    except:
        return render(request, '404.html')

    return render(request, 'trainers/trainerprofile_locations.html', context)


def delete_location(request, id):
    location = Location.objects.get(id=id)
    location.delete()
    return redirect('trainer_profile_locations')


def upload_trainer_profile(request):
    # TODO: all the upload logic goes here
    context = {
        'page_title': 'Edit trainer profile',
    }
    return render(request, 'trainers/trainerprofile_upload.html', context)


def mark_favorite(request, id):
    user = request.user
    # only logged in "normal" users can mark as favorite
    if not user.is_authenticated or user.role != Roles.USER:
        return render(request, '404.html')

    trainer = get_object_or_404(Trainer, id=id)
    if trainer.is_flagged(user):
        trainer.remove_flag(user)
    else:
        trainer.set_flag(user)

    return redirect('trainer_profile', trainer.id)
