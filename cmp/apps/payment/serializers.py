from rest_framework import serializers
from .models import Payment

class PaymentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['external_id', 'score']

class CustomerGetPostResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['external_id', 'score', 'pre_approved_at', 'status']

