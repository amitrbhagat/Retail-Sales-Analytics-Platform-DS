from django.urls import path
from .views import CustomerViewSet

customer_list=CustomerViewSet.as_view({
    "get":"list",
    "post":"create"
})

customer_detail=CustomerViewSet.as_view({
    "get":"retrieve",
    "put":"update",
    "patch":"partial_update",
    "delete":"destroy"
})

urlpatterns=[

    path("",customer_list),

    path("<int:pk>/",customer_detail)

]