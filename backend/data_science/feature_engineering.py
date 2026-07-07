import pandas as pd
import numpy as np


df = pd.read_csv("data_science/cleaned_data/clean_sales.csv")


df["invoice_date"] = pd.to_datetime(
    df["invoice_date"]
)

df["revenue"] = df["quantity"] * df["price"] 

#--------------------------Generate Date Features---------------------------------

df["month"] = df["invoice_date"].dt.month
df["day"] = df["invoice_date"].dt.day
df["week"] = df["invoice_date"].dt.isocalendar().week
df["quarter"] = df["invoice_date"].dt.quarter
df["year"] = df["invoice_date"].dt.year


#-----------------------Season Features------------------------------------

def get_season(month):

    if month in [12, 1, 2]:
        return "Winter"
    
    elif month in [3,4,5]:
        return "Spring"

    elif month in [6,7,8]:
        return "Summer"

    return "Autumn"

df["season"] = df["month"].apply(get_season)


#----------------------Weekend feature------------------------------

df["is_weekend"] = (
    df["invoice_date"].dt.weekday>=5
).astype(int)


#---------------------Holiday feature-------------------------------
df["is_holiday"] = 0


#---------------------Promotion feature-------------------------------
df["promotion"] = 0


#----------------------Lag Feature-----------------------------------
df = df.sort_values("invoice_date")

df["lag_1"] = (df["quantity"].shift(1))


#----------------------Rollling Average-----------------------------------
df["rolling_avg_7"] = (
    df["quantity"].rolling(7).mean()
)


df = pd.get_dummies(
    df,
    columns=["season"],
    dtype = int
)

df = df.fillna(0)

feature_columns = [

    "quantity",

    "price",

    "month",

    "day",

    "week",

    "quarter",

    "year",

    "is_weekend",

    "is_holiday",

    "promotion",

    "lag_1",

    "rolling_avg_7",

    "season_Autumn",

    "season_Spring",

    "season_Summer",

    "season_Winter",

    "revenue"

]

training_df = df[feature_columns]

print(training_df.head())

print(training_df.shape)

training_df.to_csv(
    "data_science/feature_data/training_dataset.csv",
    index=False
)

print("Training dataset saved successfully.")
