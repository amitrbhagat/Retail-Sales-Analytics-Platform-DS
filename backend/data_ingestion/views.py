import pandas as pd

from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Dataset
from .serializers import DatasetSerializer

from .models import RawSale
from django.utils import timezone



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
            dataset.delete()

            return Response(
                {
                    "error":f"Missing columns: {missing}"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
       
        df = df.dropna(subset=["Customer ID"])
        df = df.drop_duplicates()
        df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
        df["InvoiceDate"] = df["InvoiceDate"].apply(
            lambda x: timezone.make_aware(x)
        )
        df["Customer ID"] = df["Customer ID"].astype(int)
        print(df["InvoiceDate"].dtype)

        print(df.shape)

        raw_sales = []

        for _, row in df.iterrows():
            raw_sales.append(
                RawSale(
                    dataset=dataset,
                    invoice=row["Invoice"],
                    stock_code=row["StockCode"],
                    description=row["Description"],
                    quantity=row["Quantity"],
                    invoice_date=row["InvoiceDate"],
                    price=row["Price"],
                    customer_id=str(row["Customer ID"]),
                    country=row["Country"],
                )
            )
        print(len(raw_sales))    
        try:
            RawSale.objects.bulk_create(raw_sales, batch_size=5000)
            print("Inserted successfully")
        except Exception as e:
            print(type(e))
            print(e) 

        return Response(
            {
                "message": "Dataset imported successfully",
                "rows_imported": len(raw_sales)
            },
            status=status.HTTP_201_CREATED
        )    