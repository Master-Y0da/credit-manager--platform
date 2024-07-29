from django.db import models
from cmp.apps.models import TimestampedModel


class Customer(TimestampedModel):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    external_id = models.CharField(max_length=255, unique=True, null=False)
    score = models.IntegerField(null=False, default=0)
    pre_approved_at = models.DateTimeField(auto_now_add=True)
    status = models.SmallIntegerField(choices=[(1,1),(2,2)], default=1)

