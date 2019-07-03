from datetime import datetime
from django.db import models
from django.forms.models import model_to_dict as _model_to_dict
from lib import apidate
import uuid

def model_to_dict_with_date_support(m):
    d = _model_to_dict(m)
    for k, v in d.items():
        if isinstance(v, datetime):
            v = apidate.convert_datetime_to_iso_string(v)
    return d

class BaseManager(models.Manager):
    def get_queryset(self):
        return super(BaseManager, self).get_queryset().filter(deleted_at__isnull=True)

class BaseModel(models.Model):
    class Meta:
        abstract = True
        default_permissions = ['add', 'change', 'delete', 'view']

    created_at = models.DateTimeField(editable=False, auto_now_add=True)
    modified_at = models.DateTimeField(editable=False, auto_now_add=True)
    deleted_at = models.DateTimeField(editable=False, null=True, db_index=True)
    reference_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    objects = BaseManager()
    original_objects = models.Manager()

    def delete(self, *args, **kwargs):
        self.deleted_at = apidate.today_in_local_timezone()
        self.save()

    def model_to_dict(self):
        return model_to_dict_with_date_support(self)