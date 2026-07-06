import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("data_science/cleaned_data/clean_sales.csv")

print(df.head())
print(df.shape)


print(df.info())
print(df.describe())
print(df.isnull().sum())

#--------------------------Monthly Sales--------------------------------------

monthly_sales = (
    df.groupby("month")["quantity"].sum()
)
print(monthly_sales)

monthly_sales.plot(
    kind="line",
    figsize=(10, 5),
    title="Monthly Sales"
)

plt.savefig("data_science/visualizations/monthly_sales.png")

plt.close()


#-------------------------Yearly Sales------------------------------------

yearly_sales = (
    df.groupby("year")["quantity"].sum()
)
print(yearly_sales)

yearly_sales.plot(
    kind="bar",
    figsize=(10, 5),
    title="Yearly Sales",
)

plt.savefig("data_science/visualizations/yearly_sales.png")

plt.close()

#----------------Revenue--------------------

df["revenue"] = df["quantity"]*df["price"]
print(df["revenue"].sum())


#-----------------------Product Performance-----------------------------

top_products = (
    df.groupby("description")["revenue"].sum().sort_values(ascending=False).head(10)
)

top_products.plot(kind="bar")

plt.savefig("data_science/visualizations/top_products.png")

plt.close()


#---------------------Customer Behaviour-----------------------------

top_customers = (
    df.groupby("customer_id")["revenue"].sum().sort_values(ascending=False).head(10)
)

print(top_customers)


#-----------------------Country Performance-------------------------

country_sales = (
    df.groupby("country")["revenue"].sum().sort_values(ascending=False)
)

print(country_sales.head())


#---------------------Correlation Heatmap--------------------------

plt.figure(figsize=(8, 6))

sns.heatmap(
    df[["quantity", "price", "revenue"]].corr(), 
    annot=True
)

plt.savefig("data_science/visualizations/correlation_heatmap.png")

plt.close()


#-------------------Histogram (quantity)-------------------------------------

plt.figure(figsize=(8, 6))

plt.hist(
    df["quantity"],
    bins=30
)

plt.savefig("data_science/visualizations/quantity_histogram.png")

plt.close()