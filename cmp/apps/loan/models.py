from django.db import models
from cmp.apps.models import TimestampedModel



class Loan(TimestampedModel):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    external_id = models.CharField(max_length=255, unique=True, null=False)
    amount = models.IntegerField(null=False, default=0)
    contract_version = models.CharField(max_length=255, null=True)
    status = models.SmallIntegerField(default=1, choices=[(1,1),(2,2),(3,3),(4,4)])
    outstanding = models.IntegerField(default=0)
    maximum_payment_date = models.DateTimeField(null=True)
    taken_at = models.DateTimeField(null=True)

    customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE, related_name='loans')