from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_list_or_404

from .models import Loan
from .serializers import LoanPostSerializer, LoanGetCustomerResponseSerializer
from .decorators import custom_middleware
from cmp.permissions import Permisos


class LoanViewset(viewsets.ModelViewSet):

    queryset = Loan.objects.all()
    lookup_field = 'external_id'
    permission_classes = [Permisos]
    serializer_class = LoanPostSerializer


    @custom_middleware
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance = serializer.data
        instance["customer_id"] = request.customer

        Loan.objects.create(**instance)        

        return Response(instance, status=status.HTTP_201_CREATED)


    @action(detail=False, methods=['get'], url_path='customer/(?P<external_id>[^/.]+)')
    def loan_by_customer(self, request, external_id=None):
        
        loan = get_list_or_404(Loan, customer__external_id=external_id)
        serializer= LoanGetCustomerResponseSerializer(loan, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
