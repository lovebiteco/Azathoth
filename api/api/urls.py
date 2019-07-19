"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers
from allauth.account.views import ConfirmEmailView
from azathoth import views
from azathoth.view_sets import (
    user_view, registration_view, update_fields_view, add_fields_view, fetch_near_users_view
)

from django_private_chat import urls as django_private_chat_urls

default_router = routers.DefaultRouter()
default_router.register(r'godmode', user_view.UserViewSet, base_name='godmode')
default_router.register(r'user', update_fields_view.UpdateFieldsViewSet, base_name='user')
swipes_router = routers.DefaultRouter()
swipes_router.register(r'right', add_fields_view.SwipeRightFieldsView, base_name='swiperight')
swipes_router.register(r'left', add_fields_view.AddNopesFieldsViewSet, base_name='swipeleft')
location_router = routers.DefaultRouter()
location_router.register(r'add', add_fields_view.AddLocationFieldsView, base_name='addlocation')
location_router.register(r'fetch', fetch_near_users_view.FetchNearUsersViewSet, base_name='fetchnearusers')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/v1/', include(default_router.urls)),
    url(r'^api/v1/swipe/', include(swipes_router.urls)),
    url(r'^api/v1/accounts/', include('allauth.urls')),
    url(r'^api/v1/chat/', include('django_private_chat.urls')),
    url(r'^api/v1/location/', include(location_router.urls)),
]
