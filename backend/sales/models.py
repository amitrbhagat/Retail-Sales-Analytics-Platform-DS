from django.db import models

from core.models import BaseModel
from customers.models import Customer
from products.models import Product
from stores.models import Store


class Sale(BaseModel):

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="sales"
    )

    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sales"
    )

    store = models.ForeignKey(
        Store,
        on_delete=models.PROTECT,
        related_name="sales"
    )

    quantity = models.PositiveIntegerField()

    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    discount = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
    )

    sale_date = models.DateField()

    class Meta:

        db_table = "sales"

        ordering = ["-sale_date"]

        indexes = [
            models.Index(fields=["sale_date"]),
            models.Index(fields=["store"]),
            models.Index(fields=["product"]),
        ]

    def __str__(self):
        return f"Sale #{self.id}"