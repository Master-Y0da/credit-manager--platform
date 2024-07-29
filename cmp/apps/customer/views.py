
# Create your views here.
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.db.models import Prefetch
from django.db.models import Q


from .models import Customer
from cmp.apps.loan.models import Loan
from .serializers import CustomerPostSerializer, CustomerGetBalanceSerializer,CustomerGetPostResponseSerializer
from cmp.permissions import Permisos

class CustomerViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    lookup_field = 'external_id'
    permission_classes = [Permisos]


    def get_serializer_class(self):
        if self.action == 'create':
            return CustomerPostSerializer
        if self.action in ['list', 'retrieve']:
            return CustomerGetPostResponseSerializer


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance = serializer.save()
        return Response(CustomerGetPostResponseSerializer(instance).data, status=status.HTTP_201_CREATED)


    @action(detail=True, methods=['get'], url_path='balance')
    def balance(self, request, external_id=None):
        
        customer = Customer.objects.filter(external_id=external_id)\
                    .prefetch_related(Prefetch('loans', queryset=Loan.objects.filter(Q(status=1) | Q(status=2)))).first()
        
        outstanding_loans_total = sum([loan.outstanding for loan in customer.loans.all()])

        customer_dict = customer.__dict__
        customer_dict["total_debt"] = outstanding_loans_total
        customer_dict["available_amount"] = customer.score - outstanding_loans_total

        serializer = CustomerGetBalanceSerializer(customer_dict)
        return Response(serializer.data, status=status.HTTP_200_OK)