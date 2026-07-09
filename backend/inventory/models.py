from django.db import models

from core.models import BaseModel
from products.models import Product
from stores.models import Store


class Inventory(BaseModel):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="inventories"
    )

    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name="inventories"
    )

    current_stock = models.PositiveIntegerField()

    safety_stock = models.PositiveIntegerField(
        default=20
    )

    class Meta:
        db_table = "inventory"

        ordering = ["product"]

        constraints = [
            models.UniqueConstraint(
                fields=["product", "store"],
                name="unique_product_store_inventory"
            )
        ]

        def __str__(self):
            return f"{self.product}-{self.store}"