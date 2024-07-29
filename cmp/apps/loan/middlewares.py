
from cmp.apps.customer.models import Customer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status



class LoanManagerMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request,view_func,*args,**kwargs):
        
        customer_object = Customer.objects.filter(external_id=request.data.get('customer_external_id')).prefetch_related('loans').first()
        if not customer_object:
            return Response({"error": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)
        
        if not customer_object.loans.__dict__:
            return None
        
        outstanding_loans_total = sum([loan.outstanding for loan in customer_object.loans.all()])
        
        if outstanding_loans_total + request.data.get('amount') > customer_object.score:
            return Response({"error": "Customer has outstanding loans greater than score"}, status=status.HTTP_400_BAD_REQUEST)
        
        request.customer = customer_object.id

        return None