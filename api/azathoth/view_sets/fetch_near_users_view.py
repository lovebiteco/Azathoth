from . import base
from azathoth.models import User, UserLocation
from azathoth.serializers.user_serializers import UserSerializer
from azathoth.filters import user_filter
from rest_framework.decorators import action
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from django_filters import rest_framework as filters

## GIS
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance

class FetchNearUsersViewSet(base.BaseModelViewSet):
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = user_filter.UserFilter

    @action(detail=False, method=['get'])
    def fetch_users(self, request):
        user_1_reference_id = request.user.reference_id
        last_user_location = UserLocation.objects.filter(users__reference_id=user_1_reference_id).order_by('-created_at')[0]["location"]
        queryset = UserLocation.objects.order_by('-created_at').distinct()
        queryset = queryset.exclude(users__reference_id=user_1_reference_id)
        queryset = queryset.annotate(distance=Distance('location', last_user_location)).order_by('distance')[0:100]
        final_list = []
        context = {}
        for item in queryset:
            context['id'] = item['id']
            context['reference_id'] = item['reference_id']
            context['user_id'] = item['users__reference_id']
            context['distance'] = item['distance']
            final_list.append(context)
            context = {}
        return Response(final_list, status=200)


        
