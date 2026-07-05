from django.db import models

from core.models import BaseModel


class Dataset(BaseModel):

    name = models.CharField(
        max_length=255
    )

    csv_file = models.FileField(
        upload_to="datasets/"
    )

    uploaded_by = models.CharField(
        max_length=100,
        blank=True
    )

    class Meta:

        db_table = "datasets"

    def __str__(self):
        return self.name
    