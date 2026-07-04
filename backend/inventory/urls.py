from django.urls import path
from .views import InventoryViewSet

inventory_list=InventoryViewSet.as_view({
    "get":"list",
    "post":"create"
})

inventory_detail=InventoryViewSet.as_view({
    "get":"retrieve",
    "put":"update",
    "patch":"partial_update",
    "delete":"destroy"
})

urlpatterns=[

    path("",inventory_list),

    path("<int:pk>/",inventory_detail)

]