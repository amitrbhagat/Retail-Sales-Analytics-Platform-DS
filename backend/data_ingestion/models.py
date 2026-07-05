from django.db import models

from core.models import BaseModel


class Dataset(BaseModel):

    name = models.CharField(max_length=255)

    csv_file = models.FileField(upload_to="datasets/")

    uploaded_by = models.CharField(
        max_length=100,
        blank=True
    )

    class Meta:
        db_table = "datasets"

    def __str__(self):
        return self.name


class RawSale(BaseModel):

    dataset = models.ForeignKey(
        Dataset,
        on_delete=models.CASCADE,
        related_name="raw_sales"
    )

    invoice = models.CharField(max_length=30)

    stock_code = models.CharField(max_length=30)

    description = models.CharField(max_length=300)

    quantity = models.IntegerField()

    invoice_date = models.DateTimeField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    customer_id = models.CharField(
        max_length=30,
        blank=True
    )

    country = models.CharField(max_length=100)

    class Meta:

        db_table = "raw_sales"

        indexes = [
            models.Index(fields=["invoice"]),
            models.Index(fields=["stock_code"]),
            models.Index(fields=["invoice_date"]),
        ]

    def __str__(self):
        return self.invoice