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

    class Meta:
        model = Trainer
        fields = ['sport', 'motto', 'about']
