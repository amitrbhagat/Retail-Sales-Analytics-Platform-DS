from django.contrib import admin

from .models import Sale


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "product",
        "store",
        "quantity",
        "unit_price",
        "sale_date",
    )

    list_filter = (
        "store",
        "sale_date",
    )

    search_fields = (
        "product__name",
    )