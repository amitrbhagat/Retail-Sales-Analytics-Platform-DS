from django.contrib import admin

from .models import ForecastResult


@admin.register(ForecastResult)
class ForecastResultAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "product",
        "store",
        "forecast_date",
        "predicted_sales",
        "model_name",
    )

    list_filter = (
        "model_name",
    )
    