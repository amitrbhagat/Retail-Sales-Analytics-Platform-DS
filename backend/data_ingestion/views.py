import pandas as pd

from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Dataset
from .serializers import DatasetSerializer



class DatasetViewSet(viewsets.ModelViewSet):

    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer


    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        dataset = serializer.save()
        df = pd.read_csv(dataset.csv_file.path, encoding="ISO-8859-1")

        required_columns = [
            "Invoice",
            "StockCode",
            "Description",
            "Quantity",
            "InvoiceDate",
            "Price",
            "Customer ID",
            "Country",
        ]

        missing = [
            col for col in required_columns
            if col not in df.columns
        ]

        if missing:
            dataset.delete

            return Response(
                {
                    "error":f"Mising columns: {missing}"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            {
                "message": "Dataset uploaded successfully",
                "rows": len(df)
            },
            status=status.HTTP_201_CREATED
        )    