from django.urls import path
from .views import StoreViewSet

store_list=StoreViewSet.as_view({
    "get":"list",
    "post":"create"
})

store_detail=StoreViewSet.as_view({
    "get":"retrieve",
    "put":"update",
    "patch":"partial_update",
    "delete":"destroy"
})

urlpatterns=[

    path("",store_list),

    path("<int:pk>/",store_detail)

]