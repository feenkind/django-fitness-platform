from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Trainer


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
    )

    class Meta:
        model = Trainer
        fields = ['sport', 'motto', 'about', 'visible']
