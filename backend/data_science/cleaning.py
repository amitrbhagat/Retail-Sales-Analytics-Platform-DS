import sys
import os
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "config.settings"
)
django.setup()


import pandas as pd
import numpy as np

from data_ingestion.models import RawSale 


queryset = RawSale.objects.all().values()

df = pd.DataFrame(queryset)

print(df.head())
print(df.shape)


# -----------------------------
# Remove Duplicates
# -----------------------------

df = df.drop_duplicates()


# -----------------------------
# Handle Missing Values
# -----------------------------

df = df.dropna(
    subset=[
        "customer_id",
        "description",
        "invoice_date",
        "price",
        "quantity",
    ]
)


# -----------------------------
# Fix Data Types
# -----------------------------

df["invoice_date"] = pd.to_datetime(df["invoice_date"])

df["quantity"] = pd.to_numeric(df["quantity"])

df["price"] = pd.to_numeric(df["price"])


# -----------------------------
# Remove Invalid Records
# -----------------------------

df = df[df["quantity"] > 0]

df = df[df["price"] > 0]


# -----------------------------
# Normalize Product Names
# -----------------------------

df["description"] = (

    df["description"]

    .str.strip()

    .str.upper()

)


# -----------------------------
# Normalize Country
# -----------------------------

df["country"] = (

    df["country"]

    .str.strip()

    .str.title()

)


# -----------------------------
# Normalize Dates
# -----------------------------

df["year"] = df["invoice_date"].dt.year

df["month"] = df["invoice_date"].dt.month

df["day"] = df["invoice_date"].dt.day



#-----------------------------------------------------------
#Outlier Detection  (Remove Outlier)  using IQR for quantity
#-----------------------------------------------------------

Q1 = df["quantity"].quantile(0.25)

Q3 = df["quantity"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR

upper = Q3 + 1.5 * IQR

df = df[
    (df["quantity"] >= lower)
    &
    (df["quantity"] <= upper)
]


#--------------------------------------------------------
#Outlier Detection  (Remove Outlier)  using IQR for price
#--------------------------------------------------------

Q1 = df["price"].quantile(0.25)

Q3 = df["price"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR

upper = Q3 + 1.5 * IQR

df = df[
    (df["price"] >= lower)
    &
    (df["price"] <= upper)
]

print("=" * 50)

print(df.info())

print("=" * 50)

print(df.describe())

print("=" * 50)

print(df.isnull().sum())

print("=" * 50)

print(df.shape)


df.to_csv(
    "data_science/cleaned_data/clean_sales.csv",
    index = False,
    encoding = "utf-8",
)

print("clean Dataset saved successfully")