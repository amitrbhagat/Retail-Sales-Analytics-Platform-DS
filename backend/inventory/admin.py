from django.contrib import admin

from .models import Inventory


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "product",
        "store",
        "current_stock",
    )

    list_filter = (
        "store",
    )

    search_fields = (
        "product__name",
        "store__name",
    )