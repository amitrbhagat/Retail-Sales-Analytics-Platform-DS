from django.db import models

from core.models import BaseModel



class Store(BaseModel):

    name = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    address = models.TextField()

    manager_name = models.TextField(
        max_length=150,
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        db_table = "stores"

        ordering = ["name"]

        indexes = [
            models.Index(fields=["city"]),
        ]

        def _str_(self):
            return self.name
