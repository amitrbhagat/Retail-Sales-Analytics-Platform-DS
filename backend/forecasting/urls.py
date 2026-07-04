from django.urls import path
from .views import ForecastResultViewSet

forecastResult_list=ForecastResultViewSet.as_view({
    "get":"list",
    "post":"create"
})

forecastResult_detail=ForecastResultViewSet.as_view({
    "get":"retrieve",
    "put":"update",
    "patch":"partial_update",
    "delete":"destroy"
})

urlpatterns=[

    path("",forecastResult_list),

    path("<int:pk>/",forecastResult_detail)

]