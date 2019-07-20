from . import base
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def login_successful(request):
    return Response("Login successful.", status=200)

