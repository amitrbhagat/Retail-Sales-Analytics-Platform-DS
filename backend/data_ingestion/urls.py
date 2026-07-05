from django.urls import path

from .views import DatasetViewSet


dataset_list = DatasetViewSet.as_view({
    "get": "list",
    "post": "create",
})

urlpatterns = [

    path(
        "",
        dataset_list,
        name="dataset-upload",
    ),
]
