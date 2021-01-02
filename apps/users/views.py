from django.shortcuts import render
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from apps.users.forms import UserSettings

# Create your views here.
def user_profile(request):
    user = request.user
    if not user.is_authenticated:
        return render(
            request,
            'users/userprofile.html',
            {
                'page_title': _('Please login'),
            },
        )

    if request.method == 'POST':
        form = UserSettings(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, _('Settings saved'))
        #   # use name from urls again, redirect to a_name
        #   return HttpResponseRedirect(reverse_lazy('a_name'))
        else:
            messages.error(request, _('We had problems saving your changes.'))
    else:
        form = UserSettings(instance=user)

    return render(
        request,
        'users/userprofile.html',
        {
            'page_title': f'Settings {user.username}',
            'form': form,
        },
    )
