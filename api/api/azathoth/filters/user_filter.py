from lib.filters import BaseFilterSet, CharInFilter, IntegerFilter
from django_filters import rest_framework as filters
from azathoth.models import User


class UserFilter(BaseFilterSet):
    reference_id = CharInFilter(method='filter_reference_id', required=False)

    class Meta:
        model = User
        fields = [
            'id', 'reference_id', 'first_name', 'last_name', 'email',
            'date_of_birth', 'gender', 'last_access', 'last_known_position',
            'preferences', 'bio', 'likes', 'nopes', 'blocked', 'matched'
        ]

    def filter_reference_id(self, queryset, name, value):
        if len(value) > 0:
            queryset = queryset.filter(reference_id=value[0])
        return queryset