from django.db import models

from core.models import BaseModel


class Customer(BaseModel):

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    email = models.EmailField(
        unique=True
    )

    phone = models.CharField(
        max_length=15,
        unique=True
    )

    gender = models.CharField(
        max_length=10,
        blank=True
    )

    class Meta:
        db_table = "customers"

        ordering = ["first_name", "last_name"]

        indexes = [
            models.Index(fields=["email"]),
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"