from rest_framework import viewsets

from .models import Inventory
from .serializers import InventorySerializer


class InventoryViewSet(viewsets.ModelViewSet):

    queryset=Inventory.objects.select_related(
        "product",
        "store"
    )

    serializer_class=InventorySerializer

    filterset_fields=[
        "store",
        "product"
    ]

    search_fields=[
        "product__name",
        "store__name"
    ]

    ordering_fields="__all__"
