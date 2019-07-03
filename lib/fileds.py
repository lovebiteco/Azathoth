from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models.fields.related import ReverseOneToOneDescriptor
from rest_framework import serializers
from django.utils.encoding import smart_text

class ProtectedForeignKey(models.ForeignKey):

    def __init__(self, *args, **kwargs):
        kwargs['on_delete'] = models.PROTECT
        super(ProtectedForeignKey, self).__init__(*args, **kwargs)
