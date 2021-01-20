import magic
from django import forms
from django.core.exceptions import ValidationError
from django.template.defaultfilters import filesizeformat
from django.utils.translation import gettext_lazy as _

from fitnessplatform import settings
from .models import Trainer, Location, Upload


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


def validate_upload(file):
    content_type = magic.from_buffer(file.read(), mime=True)
    print(content_type)
    if not content_type in settings.CONTENT_TYPES:
        raise forms.ValidationError(_(
            'File type is not supported. Please upload only files of the following types: %s') % (
                                        settings.CONTENT_TYPES))
    if file.size > settings.MAX_UPLOAD_SIZE:
        raise forms.ValidationError(
            _('Please keep the filesize under %s. Current filesize: %s') % (
                filesizeformat(settings.MAX_UPLOAD_SIZE),
                filesizeformat(file.size)))


class UploadForm(forms.ModelForm):
    title = forms.CharField(required=True, label=_('Title'))
    url = forms.FileField(required=True, label='', validators=[validate_upload], )

    class Meta:
        model = Upload
        fields = ['title', 'url']
