from view_sets import base
from azathoth.serializers.user_serializers import UserSerializer
from azatoth.filters import user_filter
from azathoth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from knox.auth import TokenAuthentication
from django_filters import rest_framework as filters

class UserViewSet(base.BaseModelViewSet):
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = user_filter.UserFilter

    @action(detail=False, methods=['post'])
    def add_new_student(self, request):
        first_name = self.request.data.get('first_name', None)
        last_name = self.request.data.get('last_name', None)
        email = self.request.data.get('email', None)
        


    def get_queryset(self):
        queryset = User.objects.all().distinct()
        return queryset