import django_filters
from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from apps.trainers.models import *


class TrainerFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='name',
        label=_('Trainer name'),
        method='filter_trainer_name',
    )

    city = django_filters.ModelChoiceFilter(
        label=_('Location'),
        queryset=Location.objects.values_list('city', flat=True).distinct(),
        field_name='location__city',
        to_field_name='city',
    )

    # first or last name can contain given value
    def filter_trainer_name(self, queryset, name, value):
        return queryset.filter(
            Q(user_id__first_name__icontains=value)
            | Q(user_id__last_name__icontains=value)
        )

    class Meta:
        model = Trainer
        fields = {
            'sport': ['exact'],
        }
