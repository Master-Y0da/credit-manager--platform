from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_list_or_404

from .models import Payment
from .serializers import PaymentPostSerializer, LoanGetCustomerResponseSerializer
from cmp.permissions import Permisos


class PaymentViewset(viewsets.ModelViewSet):

    queryset = Payment.objects.all()
    lookup_field = 'external_id'
    permission_classes = [Permisos]
    serializer_class = PaymentPostSerializer

