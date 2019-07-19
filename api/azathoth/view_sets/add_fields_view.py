from . import base
from azathoth.serializers.user_serializers import UserSerializer, UserLikesSerializer, UserNopesSerializer, UserMatchedSerializer
from azathoth.filters import user_filter, user_likes_filter, user_nopes_filter, user_matched_filter
from azathoth.models import User, UserLikes, UserNopes, UserMatched
from rest_framework.decorators import action
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from django_filters import rest_framework as filters
from datetime import datetime

class AddNopesFieldsViewSet(base.BaseModelViewSet):
    serializer_class = UserNopesSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = user_nopes_filter.UserFilter

    @action(detail=False, methods=['post'])
    def add_to_nopes_pool(self, request):
        user_1_reference_id = request.user.reference_id
        request_data = request.data
        user_2_reference_id = request_data["user_2_ref_id"]
        new_nope = UserNopes(noped_user=user_2_reference_id, noped_at=datetime.now())
        new_nope.save()
        user_1 = User.objects.get(reference_id=user_1_reference_id)
        new_nope.users.add(user_1)
        return Response("Query added.")

class AddMatchesFieldsViewSet(base.BaseModelViewSet):
    serializer_class = UserMatchedSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = user_matched_filter.UserFilter

    @action(detail=False, methods=['post'])
    def add_to_matched_pool(self, request):
        user_1_reference_id = request.user.reference_id
        request_data = request.data
        user_2_reference_id = request_data["user_2_ref_id"]
        new_match = UserMatched(matched_user=user_2_reference_id, matched_at=datetime.now())
        new_match.save()
        user_1 = User.objects.get(reference_id=user_1_reference_id)
        new_match.users.add(user_1)
        return Response("Query added.")


class SwipeRightFieldsView(base.BaseModelViewSet):
    serializer_class = UserLikesSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = user_likes_filter.UserFilter

    @action(detail=False, methods=['post'])
    def add_to_like_pool(self, request):
        user_1_reference_id = request.user.reference_id
        request_data = request.data
        user_2_reference_id = request_data["user_2_ref_id"]
        new_like = UserLikes(liked_user=user_2_reference_id, liked_at=datetime.now())
        new_like.save()
        user_1 = User.objects.get(reference_id=user_1_reference_id)
        new_like.users.add(user_1)
        return Response("Query added.")

    @action(detail=False, methods=['post'])
    def add_to_swipe_right(self, request):
        user_1_reference_id = request.user.reference_id
        request_data = request.data
        user_2_reference_id = request_data["user_2_ref_id"]
        if UserLikes.objects.filter(users__reference_id=user_2_reference_id, liked_user=user_1_reference_id).exists():
            ## The other user already likes user 1, add to match.
            new_match = UserMatched(matched_user=user_2_reference_id, matched_at=datetime.now())
            new_match.save()
            user_1 = User.objects.get(reference_id=user_1_reference_id)
            new_match.users.add(user_1)
            return Response("Query added.")
        else:
            ## Other user does not already like user 1, or just fucking hates him. IDK. I don't read minds.
            ## Anyway, add to likes.
            ## By the way, Hi from London. It's pouring. As always.
            new_like = UserLikes(liked_user=user_2_reference_id, liked_at=datetime.now())
            new_like.save()
            user_1 = User.objects.get(reference_id=user_1_reference_id)
            new_like.users.add(user_1)
            return Response("Query added.")







    

