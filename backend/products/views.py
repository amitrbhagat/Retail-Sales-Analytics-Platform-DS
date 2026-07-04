from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.select_related("category")

    serializer_class = ProductSerializer

    filterset_fields = [
        "category",
        "brand",
        "is_active",
    ]

    search_fields = [
        "name",
        "sku",
        "brand",
    ]

    ordering_fields = [
        "name",
        "unit_price",
    ]
    