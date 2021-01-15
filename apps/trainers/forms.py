from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Trainer, Location, Upload_File


class TrainerSettings(forms.ModelForm):
    sport = forms.ChoiceField(choices=Trainer.Sports.choices)
    motto = forms.CharField(label=_('Motto'))
    about = forms.CharField(
        widget=forms.Textarea,
        help_text=_('Text can only be 500 characters long.'),
        label=_('About me'),
    )
    visible = forms.BooleanField(
        label=_(
            'Profile is visible',
        ),
        help_text=(
            'When this is checked, the profile is visible for all users of trainhorizon and will also appear in the trainer overview.'
        ),
        required=False,
    )

    class Meta:
        model = Trainer
        fields = ['sport', 'motto', 'about', 'visible']


class LocationSettings(forms.ModelForm):
    name = forms.CharField(label=_('Studio Name'))
    street = forms.CharField(label=_('Street'))
    number = forms.CharField(label=_('Number'))
    zipcode = forms.CharField(label=_('Zipcode'))
    city = forms.CharField(label=_('City'))
    country = forms.CharField(label=_('Country'))

    class Meta:
        model = Location
        fields = ['name', 'street', 'number', 'zipcode', 'city', 'country']


class UploadForm(forms.ModelForm):
    title = forms.CharField(label=_('Title'))
    uploaded = forms.FileField(required=True, help_text= "You can't upload without an upload.")
    class Meta:
        model = Upload_File
        fields = ['title', 'uploaded']
