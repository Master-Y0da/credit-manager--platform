from rest_framework import serializers
from .models import Customer

class CustomerPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['external_id', 'score']

class CustomerGetPostResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['external_id', 'score', 'pre_approved_at', 'status']


class CustomerGetBalanceSerializer(serializers.ModelSerializer):

    total_debt = serializers.IntegerField()
    available_amount = serializers.IntegerField()

    class Meta:
        model = Customer
        fields = ['external_id', 'score', 'total_debt', 'available_amount']
