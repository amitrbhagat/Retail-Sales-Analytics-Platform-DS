from django.urls import path
from .views import SaleViewSet

sale_list=SaleViewSet.as_view({
    "get":"list",
    "post":"create"
})

sale_detail=SaleViewSet.as_view({
    "get":"retrieve",
    "put":"update",
    "patch":"partial_update",
    "delete":"destroy"
})

urlpatterns=[

    path("",sale_list),

    path("<int:pk>/",sale_detail)

]