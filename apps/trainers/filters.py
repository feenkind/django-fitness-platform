import django_filters
from apps.trainers.models import *
from django.utils.translation import gettext_lazy as _


class TrainerFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='user_id__first_name',
        label=_('Trainer name'),
        lookup_expr='icontains',
        method='filter_trainer_name',
    )

    def filter_trainer_name(self, queryset, name, value):
        return queryset

    class Meta:
        model = Trainer
        fields = {
            'sport': ['exact'],
        }