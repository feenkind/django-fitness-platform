from allauth.account.forms import SignupForm
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Roles, User


class UsersSignupForm(SignupForm):
    first_name = forms.CharField(
        max_length=30, label=_('First Name'), required=True
    )
    last_name = forms.CharField(
        max_length=30, label=_('Last Name'), required=True
    )

    def save(self, request):
        # Ensure you call the parent class's save.
        user = super(UsersSignupForm, self).save(request)

        # own processing
        user.role = Roles.TRAINER
        user.save()

        return user


class UserSettings(forms.ModelForm):
    username = forms.CharField(label=_('Username *'))
    email = forms.EmailField(required=True, label=_('Email *'))
    first_name = forms.CharField(required=True, label=_('First Name *'))
    last_name = forms.CharField(required=True, label=_('Email *'))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
