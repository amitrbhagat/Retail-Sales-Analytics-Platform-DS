from rest_framework import viewsets

from .models import Sale
from .serializers import SaleSerializer


class SaleViewSet(viewsets.ModelViewSet):

    queryset=Sale.objects.select_related(
        "product",
        "customer",
        "store"
    )

    serializer_class=SaleSerializer

    filterset_fields=[
        "store",
        "product",
        "sale_date"
    ]

    search_fields=[
        "product__name"
    ]

    ordering_fields=[
        "sale_date",
        "quantity"
    ]
