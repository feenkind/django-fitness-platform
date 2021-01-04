import django_filters
from apps.trainers.models import *


class TrainerFilter(django_filters.FilterSet):
    sport = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Trainer
        fields = ['sport']