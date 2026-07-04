from rest_framework import viewsets

from .models import Store
from .serializers import StoreSerializer


class StoreViewSet(viewsets.ModelViewSet):

    queryset = Store.objects.all()

    serializer_class = StoreSerializer

    filterset_fields = "__all__"

    search_fields = [
        "name",
        "city",
        "state",
    ]

    ordering_fields = "__all__"