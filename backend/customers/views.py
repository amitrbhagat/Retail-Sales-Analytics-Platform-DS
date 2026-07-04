from rest_framework import viewsets

from .models import Customer
from .serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    filterset_fields="__all__"
    search_fields=["first_name","last_name","email"]
    ordering_fields="__all__"
