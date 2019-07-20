from . import base
from azathoth.models import User, UserLocation
from azathoth.serializers.user_serializers import UserSerializer
from azathoth.filters import user_filter
from rest_framework.decorators import action
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from django_filters import rest_framework as filters

from datetime import datetime

class FetchUserDetails(base.BaseModelViewSet):
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = user_filter.UserFilter

    @action(detail=False, methods=['post'])
    def fetch_user_details(self, request):
        request_data = request.data
        user = User.objects.get(reference_id=request_data["reference_id"])
        final_list = []
        context = {}
        context['user_id'] = request_data["reference_id"]
        context['first_name'] = user.first_name
        context['last_name'] = user.last_name
        context['gender'] = user.gender
        context['university_name'] = user.university_name
        context['dept_name'] = user.dept_name
        context['description'] = user.description
        age = datetime.now().year - user.date_of_birth.year
        context['age'] = age
        final_list.append(context)
        return Response(final_list, status=200)



    

