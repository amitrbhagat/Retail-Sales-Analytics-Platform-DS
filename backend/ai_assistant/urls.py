from django.urls import path

from .views import (
    ChatView,
    ForecastView,
    InventoryView,
    AnalyticsView,
)

urlpatterns = [

    path(
        "chat/",
        ChatView.as_view(),
    ),

    path(
        "forecast/",
        ForecastView.as_view(),
    ),

    path(
        "inventory/",
        InventoryView.as_view(),
    ),

    path(
        "analytics/",
        AnalyticsView.as_view(),
    ),

]