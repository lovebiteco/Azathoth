from django.conf import settings
from django.core.paginator import Paginator
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from rest_framework.renderers import JSONRenderer
from django_filters import rest_framework as filters
#from knox.auth import TokenAuthentication
from lib.filters import BaseFilterSet, BaseRefFilterSet
from rest_framework.authentication import SessionAuthentication

#from api import models

class LoginRequiredMixin:
    #authentication_classes = [SessionAuthentication, TokenAuthentication]
    authentication_classes = [SessionAuthentication, ]
    permission_classes = [permissions.IsAuthenticated]

class BaseModelViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = BaseFilterSet
    
class BaseReadOnlyModelViewSet(LoginRequiredMixin, viewsets.ReadOnlyModelViewSet):
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = BaseFilterSet

class BaseModelRefViewSet(BaseModelViewSet):
    filter_class = BaseRefFilterSet
    lookup_field = 'ref'