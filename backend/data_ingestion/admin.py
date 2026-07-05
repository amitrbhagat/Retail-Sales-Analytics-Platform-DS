from django.contrib import admin

from .models import Dataset, RawSale


@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "uploaded_by",
        "created_at",
    )


@admin.register(RawSale)
class RawSaleAdmin(admin.ModelAdmin):

    list_display = (
        "invoice",
        "stock_code",
        "quantity",
        "price",
        "customer_id",
        "country",
    )

    search_fields = (
        "invoice",
        "stock_code",
    )