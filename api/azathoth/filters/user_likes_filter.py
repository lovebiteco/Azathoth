from lib.filters import BaseFilterSet, CharInFilter, IntegerFilter
from django_filters import rest_framework as filters
from azathoth.models import UserLikes


class UserFilter(BaseFilterSet):
    reference_id = CharInFilter(method='filter_reference_id', required=False)

    class Meta:
        model = UserLikes
        fields = [
            'id', 'reference_id', 'users', 'liked_user', 'liked_at'
        ]

    def filter_reference_id(self, queryset, name, value):
        if len(value) > 0:
            queryset = queryset.filter(reference_id=value[0])
        return queryset