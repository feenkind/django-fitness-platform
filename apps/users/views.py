from django.shortcuts import render
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from apps.users.forms import UserSettings

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
    favorite_trainers = []
    context = {
        'page_title': _('Favorite trainers'),
        'favorites': favorite_trainers,
    }

    return render(request, 'users/favorites.html', context)
