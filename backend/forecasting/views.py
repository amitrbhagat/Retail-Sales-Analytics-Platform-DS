from rest_framework import viewsets

from .models import ForecastResult
from .serializers import ForecastResultSerializer


class ForecastResultViewSet(viewsets.ModelViewSet):

    queryset=ForecastResult.objects.select_related(
        "product",
        "store"
    )

    serializer_class=ForecastResultSerializer

    filterset_fields="__all__"

    ordering_fields="__all__"