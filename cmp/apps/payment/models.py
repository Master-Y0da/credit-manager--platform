from django.db import models
from cmp.apps.models import TimestampedModel



class Payment(TimestampedModel):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    external_id = models.CharField(max_length=255, unique=True, null=False)
    total_amount = models.IntegerField(null=False, default=0)
    status = models.SmallIntegerField(choices=[(1,1),(2,2)])
    paid_at = models.DateTimeField(auto_now_add=True)

    customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE, related_name='payments')
   

class PaymentDetail(TimestampedModel):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    amount = models.IntegerField(null=False, default=0)

    payment = models.ForeignKey('payment.Payment', on_delete=models.CASCADE, related_name='details')
    loan = models.ForeignKey('loan.Loan', on_delete=models.CASCADE, related_name='payments')
    