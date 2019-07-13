from django_filters import rest_framework as filters
import uuid
from rest_framework.exceptions import ValidationError
from django.forms.fields import IntegerField

class CharInFilter(filters.BaseInFilter, filters.CharFilter):
    pass

class BaseFilterSet(filters.FilterSet):
    ids = CharInFilter(method='filter_id', required=False)

    def filter_id(self, queryset, name, value):
        return queryset.filter(pk__in=value)

    def is_valid(self):
        for name, field in self.filters.items():
            if field.extra.get('required') and name not in self.data:
                raise ValidationError('You need to filter this resource using at least the %s field' % name)
        return super().is_valid()
    
class BaseRefFilterSet(BaseFilterSet):
    def filter_id(self, queryset, name, value):
        try:
            value = list(map(lambda v: uuid.UUID(v), value))
        except ValueError:
            return queryset.none()
        return queryset.filter(ref__in=value)
        
class IntegerFilter(filters.NumberFilter):
    field_class = IntegerField
