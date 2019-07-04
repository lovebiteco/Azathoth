from lib.filters import BaseFilterSet, CharInFilter, IntegerFilter
from django_filters import rest_framework as filters
from azathoth.models import UserBio


class UserFilter(BaseFilterSet):
    reference_id = CharInFilter(method='filter_reference_id', required=False)

    class Meta:
        model = UserBio
        fields = [
            'id', 'reference_id', 'user', 'description', 'dept_name',
            'university_name', 'image_url_1', 'image_url_2', 'image_url_3',
            'image_url_4', 'image_url_5'
        ]

    def filter_reference_id(self, queryset, name, value):
        if len(value) > 0:
            queryset = queryset.filter(reference_id=value[0])
        return queryset