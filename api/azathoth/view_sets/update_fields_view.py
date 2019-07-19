from . import base
from azathoth.serializers.user_serializers import UserSerializer
from azathoth.filters import user_filter
from azathoth.models import User
from rest_framework.decorators import action
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from django_filters import rest_framework as filters
from datetime import datetime
import ast

class UpdateFieldsViewSet(base.BaseModelViewSet):
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = user_filter.UserFilter

    @action(detail=False, methods=['post'])
    def update_description(self, request):
        reference_id = request.user.reference_id
        request_data = request.data
        queryset = User.objects.filter(reference_id=reference_id)
        queryset.update(description=request_data["description"])
        queryset.update(modified_at=datetime.now())
        return Response("Query updated")
    
    @action(detail=False, methods=['post'])
    def update_dept_name(self, request):
        reference_id = request.user.reference_id
        request_data = request.data
        queryset = User.objects.filter(reference_id=reference_id)
        queryset.update(dept_name=request_data["dept_name"])
        queryset.update(modified_at=datetime.now())
        return Response("Query updated")

    @action(detail=False, methods=['post'])
    def update_university_name(self, request):
        reference_id = request.user.reference_id
        request_data = request.data
        queryset = User.objects.filter(reference_id=reference_id)
        queryset.update(university_name=request_data["university_name"])
        queryset.update(modified_at=datetime.now())
        return Response("Query updated")

    @action(detail=False, methods=['post'])
    def update_img(self, request):
        reference_id = request.user.reference_id
        request_data = request.data
        queryset = User.objects.filter(reference_id=reference_id)
        if int(request_data["img_number"]) is 1:
            queryset.update(img_url_1=request_data["img_url"])
        elif int(request_data["img_number"]) is 2:
            queryset.update(img_url_2=request_data["img_url"])
        elif int(request_data["img_number"]) is 3:
            queryset.update(img_url_3=request_data["img_url"])
        elif int(request_data["img_number"]) is 4:
            queryset.update(img_url_4=request_data["img_url"])
        elif int(request_data["img_number"]) is 5:
            queryset.update(img_url_5=request_data["img_url"])
        else:
            return Response("Image number is a required field.")
        queryset.update(bio__modified_at=datetime.now())
        return Response("Query updated")

    @action(detail=False, methods=['post'])
    def update_looking_for(self, request):
        reference_id = request.user.reference_id
        request_data = request.data
        queryset = User.objects.filter(reference_id=reference_id)
        queryset.update(looking_for=request_data["looking_for"])
        queryset.update(modified_at=datetime.now())
        return Response("Query updated")

    @action(detail=False, methods=['post'])
    def update_interested_in(self, request):
        reference_id = request.user.reference_id
        request_data = request.data
        queryset = User.objects.filter(reference_id=reference_id)
        queryset.update(interested_in=request_data["interested_in"])
        queryset.update(modified_at=datetime.now())
        return Response("Query updated")

    @action(detail=False, methods=['post'])
    def update_similar_match(self, request):
        reference_id = request.user.reference_id
        request_data = request.data
        queryset = User.objects.filter(reference_id=reference_id)
        queryset.update(similar_match = ast.literal_eval(request_data["similar_match"]))
        queryset.update(modified_at = datetime.now())
        return Response("Query updated")

    @action(detail=False, methods=['post'])
    def update_first_login(self, request):
        reference_id = request.user.reference_id
        request_data = request.data
        queryset = User.objects.filter(reference_id=reference_id)
        queryset.update(is_first_login = ast.literal_eval(request_data["first_login"]))
        queryset.update(modified_at = datetime.now())
        return Response("Query updated")

    @action(detail=False, methods=['post'])
    def update_name(self, request):
        reference_id = request.user.reference_id
        request_data = request.data
        queryset = User.objects.filter(reference_id=reference_id)
        if request_data["first_name"] is not "":
            queryset.update(first_name=request_data["first_name"])
        if request_data["last_name"] is not "":
            queryset.update(last_name=request_data["last_name"])
        queryset.update(modified_at = datetime.now())
        return Response("Query updated")
    
    @action(detail=False, methods=['post'])
    def update_gender(self, request):
        reference_id = request.user.reference_id
        request_data = request.data
        queryset = User.objects.filter(reference_id=reference_id)
        if request_data["gender"] is not "":
            queryset.update(gender=request_data["gender"])
        queryset.update(modified_at = datetime.now())
        return Response("Query updated")

    @action(detail=False, methods=['post'])
    def update_last_known_position(self, request):
        reference_id = request.user.reference_id
        request_data = request.data
        queryset = User.objects.filter(reference_id=reference_id)
        if request_data["last_known_position"] is not "":
            queryset.update(last_known_position=request_data["last_known_position"])
        queryset.update(modified_at = datetime.now())
        return Response("Query updated")


