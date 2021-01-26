from django.shortcuts import render
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from siteflags.models import ModelWithFlag
from apps.users.forms import UserSettings
from apps.users.models import Roles
from apps.trainers.models import Trainer

# Create your views here.
def user_profile(request):
    user = request.user
    if not user.is_authenticated:
        context = {'page_title': _('Please login')}
        return render(request, 'users/userprofile.html', context)

    if request.method == 'POST':
        form = UserSettings(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, _('Settings saved'))
            return HttpResponseRedirect(reverse_lazy('user_profile'))
        else:
            messages.error(request, _('We had problems saving your changes.'))
    else:
        form = UserSettings(instance=user)

    context = {
        'page_title': f'Settings {user.username}',
        'form': form,
    }
    return render(request, 'users/userprofile.html', context)


def get_user_favorites(request):
    user = request.user

    if hasattr(user, 'role') and user.role != Roles.USER:
        return render(request, '404.html')

    # this returns all trainers with flags, the ones not flagged for the user have no value though
    flagged_trainers = ModelWithFlag.get_flags_for_objects(
        Trainer.objects.all(), user
    )
    # filter these trainers only for the ones with flag value, this is the one where trainer object is not empty
    favorite_trainer_ids = [
        trainer_id
        for (trainer_id, trainer) in list(flagged_trainers.items())
        if len(trainer) > 0
    ]
    # another query is probably faster than a loop
    # get the favorite trainer objects
    favorite_trainers = Trainer.objects.filter(
        id__in=favorite_trainer_ids, visible=True
    )

    context = {
        'page_title': _('Favorite trainers'),
        'favorites': favorite_trainers,
    }

    return render(request, 'users/favorites.html', context)
