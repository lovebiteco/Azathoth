from . import base
from azathoth.serializers.user_serializers import UserSerializer
#from filters import user_filter
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
    #authentication_classes = [TokenAuthentication]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = user_filter.UserFilter

    @action(detail=False, methods=['post'])
    def update_description(self, request):
        reference_id = request.user.reference_id
        description = request.POST.get("description", "")
        queryset = User.objects.filter(reference_id=reference_id)
        queryset.update(bio__description=description)
        queryset.update(bio__modified_at=datetime.now())
        queryset.save()
        return Response("Query updated")
    
    @action(detail=False, methods=['post'])
    def update_dept_name(self, request):
        reference_id = request.user.reference_id
        dept_name = request.POST.get("dept_name", "")
        queryset = User.objects.filter(reference_id=reference_id)
        queryset.update(bio__dept_name=dept_name)
        queryset.update(bio__modified_at=datetime.now())
        queryset.save()
        return Response("Query updated")

    @action(detail=False, methods=['post'])
    def update_university_name(self, request):
        reference_id = request.user.reference_id
        university_name = request.POST.get("university_name", "")
        queryset = User.objects.filter(reference_id=reference_id)
        queryset.update(bio__university_name=university_name)
        queryset.update(bio__modified_at=datetime.now())
        queryset.save()
        return Response("Query updated")

    @action(detail=False, methods=['post'])
    def update_img(self, request):
        reference_id = request.user.reference_id
        img_url = request.POST.get("img_url", "")
        img_number = request.POST.get("img_number", "")
        queryset = User.objects.filter(reference_id=reference_id)
        if int(img_number) is 1:
            queryset.update(bio__img_url_1=img_url)
        elif int(img_number) is 2:
            queryset.update(bio__img_url_2=img_url)
        elif int(img_number) is 3:
            queryset.update(bio__img_url_3=img_url)
        elif int(img_number) is 4:
            queryset.update(bio__img_url_4=img_url)
        elif int(img_number) is 5:
            queryset.update(bio__img_url_5=img_url)
        else:
            return Response("Image number is a required field.")
        queryset.update(bio__modified_at=datetime.now())
        queryset.save()
        return Response("Query updated")

    @action(detail=False, methods=['post'])
    def update_looking_for(self, request):
        reference_id = request.user.reference_id
        looking_for = request.POST.get("looking_for", "")
        queryset = User.objects.filter(reference_id=reference_id)
        queryset.update(preferences__looking_for=looking_for)
        queryset.update(preferences__modified_at=datetime.now())
        queryset.save()
        return Response("Query updated")

    @action(detail=False, methods=['post'])
    def update_interested_in(self, request):
        reference_id = request.user.reference_id
        interested_in = request.POST.get("interested_in", "")
        queryset = User.objects.filter(reference_id=reference_id)
        queryset.update(preferences__interested_in=interested_in)
        queryset.update(preferences__modified_at=datetime.now())
        queryset.save()
        return Response("Query updated")

    @action(detail=False, methods=['post'])
    def update_similar_match(self, request):
        reference_id = request.user.reference_id
        similar_match = request.POST.get("similar_match", "False")
        queryset = User.objects.filter(reference_id=reference_id)
        queryset.update(preferences__similar_match = ast.literal_eval(similar_match))
        queryset.update(preferences__modified_at = datetime.now())
        queryset.save()
        return Response("Query updated")

    @action(detail=False, methods=['post'])
    def update_first_login(self, request):
        reference_id = request.user.reference_id
        first_login = request.POST.get("first_login", "True")
        queryset = User.objects.filter(reference_id=reference_id)
        queryset.update(is_first_login = ast.literal_eval(first_login))
        queryset.update(modified_at = datetime.now())
        queryset.save()
        return Response("Query updated")

    @action(detail=False, methods=['post'])
    def update_name(self, request):
        reference_id = request.user.reference_id
        first_name = request.POST.get("first_name", "")
        last_name = request.POST.get("last_name", "")
        queryset = User.objects.filter(reference_id=reference_id)
        if first_name is not "":
            queryset.update(first_name=first_name)
        if last_name is not "":
            queryset.update(last_name=last_name)
        queryset.update(modified_at = datetime.now())
        queryset.save()
        return Response("Query updated")
    
    @action(detail=False, methods=['post'])
    def update_gender(self, request):
        reference_id = request.user.reference_id
        gender = request.POST.get("gender", "")
        queryset = User.objects.filter(reference_id=reference_id)
        if gender is not "":
            queryset.update(gender=gender)
        queryset.update(modified_at = datetime.now())
        queryset.save()
        return Response("Query updated")


