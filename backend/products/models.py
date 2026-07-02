from django.db import models

from core.models import BaseModel
from categories.models import Category


class Product(BaseModel):

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="products"
    )

    name = models.CharField(
        max_length=255
    )

    sku = models.CharField(
        max_length=50, 
        unique=True
    )

    brand = models.CharField(
        max_length=100,
        blank=True
    )

    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    cost_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:

        db_table = "products"
        ordering = ["name"]

        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["sku"]),
        ]

    def _str_(self):
        return self.name    