from allauth.account.forms import SignupForm
from django import forms
from .models import Roles


class UsersSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name', initial='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name', initial='Last Name')

    def save(self, request):
        # Ensure you call the parent class's save.
        user = super(UsersSignupForm, self).save(request)

        # own processing
        user.role = Roles.TRAINER
        user.save()

        return user
