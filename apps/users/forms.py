from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as AllauthSocialSignupForm
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Roles, User


class UsersSignupForm(SignupForm):
    first_name = forms.CharField(
        max_length=30,
        label=_('First Name* '),
        required=True,
        widget=forms.TextInput(attrs={'placeholder': _('First Name')}),
    )
    last_name = forms.CharField(
        max_length=30,
        label=_('Last Name *'),
        required=True,
        widget=forms.TextInput(attrs={'placeholder': _('Last Name')}),
    )

    role = forms.ChoiceField(
        choices=(
            ('user', _('No, I want to register as a normal user')),
            ('trainer', _('Yes I want to register as a trainer')),
        ),
        required=True,
        label=_('Do you want to offer training classes? *'),
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
        user.role = (
            Roles.TRAINER
            if self.cleaned_data['role'] == 'trainer'
            else Roles.USER
        )
        user.save()

        return user


class UserSettings(forms.ModelForm):
    email = forms.EmailField(required=True, label=_('Email *'))
    first_name = forms.CharField(required=True, label=_('First Name *'))
    avatar = forms.ImageField(
        required=False,
        help_text=_('For best results make sure to upload a square image.'),
    )
    last_name = forms.CharField(required=True, label=_('Last Name *'))

    class Meta:
        model = User
        fields = ['avatar', 'username', 'email', 'first_name', 'last_name']
        labels = {
            'username': _('Username *'),
        }


class SocialSignupForm(AllauthSocialSignupForm):
    first_name = forms.CharField(
        max_length=30,
        label=_('First Name* '),
        required=True,
        widget=forms.TextInput(attrs={'placeholder': _('First Name')}),
    )
    last_name = forms.CharField(
        max_length=30,
        label=_('Last Name *'),
        required=True,
        widget=forms.TextInput(attrs={'placeholder': _('Last Name')}),
    )

    role = forms.ChoiceField(
        choices=(
            ('user', _('No, I want to register as a normal user')),
            ('trainer', _('Yes I want to register as a trainer')),
        ),
        required=True,
        label=_('Do you want to offer training classes? *'),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = _('E-mail *')
        self.fields['username'].label = _('Username *')

    def save(self, request):
        user = super(SocialSignupForm, self).save(request)
        user.role = (
            Roles.TRAINER
            if self.cleaned_data['role'] == 'trainer'
            else Roles.USER
        )
        user.save()
        return user