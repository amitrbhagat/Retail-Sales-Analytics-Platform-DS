from django.contrib import admin

from .models import Store


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "city",
        "state",
        "is_active",
    )

    list_filter = (
        "city",
        "state",
        "is_active",
    )

    search_fields = (
        "name",
        "city",
    )