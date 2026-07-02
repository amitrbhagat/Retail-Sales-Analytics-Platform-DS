from django.db import models

from core.models import BaseModel
from products.models import Product
from stores.models import Store


class ForecastResult(BaseModel):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="forecasts"
    )

    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name="forecasts"
    )

    forecast_date = models.DateField()

    predicted_sales = models.FloatField()

    model_name = models.CharField(
        max_length=100
    )

    confidence_score = models.FloatField()

    class Meta:

        db_table = "forecast_results"

        ordering = ["-forecast_date"]

    def __str__(self):
        return f"{self.product} - {self.forecast_date}"