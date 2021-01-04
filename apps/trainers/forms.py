from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Trainer


class TrainerSettings(forms.ModelForm):
    sport = forms.ChoiceField(choices=Trainer.Sports.choices)
    motto = forms.CharField(label=_('Motto'))
    about = forms.CharField(label=_('About'))

    class Meta:
        model = Trainer
        fields = ['sport', 'motto', 'about']
