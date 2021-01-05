from allauth.account.forms import SignupForm
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Roles, User


class UsersSignupForm(SignupForm):
    first_name = forms.CharField(
        max_length=30,
        label=_('First Name* '),
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'First Name'}),
    )
    last_name = forms.CharField(
        max_length=30,
        label=_('Last Name *'),
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = _('E-mail *')
        self.fields['username'].label = _('Username *')
        self.fields['password1'].label = _('Password *')
        self.fields['password2'].label = _('Password (again) *')

    def save(self, request):
        # Ensure you call the parent class's save.
        user = super(UsersSignupForm, self).save(request)

        # own processing
        user.role = Roles.TRAINER
        user.save()

        return user


class UserSettings(forms.ModelForm):
    email = forms.EmailField(required=True, label=_('Email *'))
    first_name = forms.CharField(required=True, label=_('First Name *'))
    avatar = forms.ImageField(required=False)
    last_name = forms.CharField(required=True, label=_('Last Name *'))

    class Meta:
        model = User
        fields = ['avatar', 'username', 'email', 'first_name', 'last_name']
        labels = {
            'username': _('Username *'),
        }
