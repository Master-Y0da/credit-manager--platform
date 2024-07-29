from rest_framework import serializers
from .models import Loan

class LoanPostSerializer(serializers.ModelSerializer):

    customer_external_id = serializers.CharField(write_only=True,source='customer.external_id')

    class Meta:
        model = Loan
        fields = ['external_id','amount','outstanding','customer_external_id']

class LoanGetCustomerResponseSerializer(serializers.ModelSerializer):
    customer_external_id = serializers.CharField(write_only=False,source='customer.external_id')
    class Meta:
        model = Loan
        fields = ['external_id','status', 'customer_external_id','outstanding','amount']
