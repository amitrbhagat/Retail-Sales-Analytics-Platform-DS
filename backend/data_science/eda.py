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


#----------------------Profit Analysis---------------------------------------

df["profit"] = df["revenue"] * 0.30
print("Total Profit :", df["profit"].sum())

monthly_profit = (
    df.groupby("month")["profit"].sum()
)

monthly_profit.plot(
    kind="line",
    figsize=(10,5),
    title="Monthly Profit"
)

plt.savefig(
    "data_science/visualizations/monthly_profit.png"
)

plt.close()


#-----------------------Category Trends (stock code)-----------------------

category_trends = (
    df.groupby("stock_code")["revenue"].sum().sort_values(ascending=False).head(10)
)

category_trends.plot(kind="bar")

plt.savefig("data_science/visualizations/category_trends.png")

plt.close()


#--------------------Pie Chart (Country Sales)--------------------------------------------

country_sales = (
    df.groupby("country")["revenue"].sum().sort_values(ascending=False).head(5)
)

country_sales.plot(
    kind="pie",
    autopct = "%1.1f%%"
)

plt.ylabel("")

plt.savefig("data_science/visualizations/country_sales_pie.png")

plt.close()


#-------------------Price Distribution plot------------------------------------------------

plt.figure(figsize=(8, 5))

sns.histplot(
    df["price"],
    bins = 30,
    kde = True
)

plt.savefig("data_science/visualizations/price_distribution.png")

plt.close()


#--------------------Business KPIs-------------------------------------------------

print("=" * 50)

print("Business KPIs")

print("=" * 50)

print("Total Revenue :", df["revenue"].sum())

print("Total Profit :", df["profit"].sum())

print("Total Orders :", df["invoice"].nunique())

print("Total Customers :", df["customer_id"].nunique())

print("Total Products :", df["stock_code"].nunique())

print("Average Order Value :",
      df["revenue"].sum() / df["invoice"].nunique())



#--------------------------EDA findings Report-------------------------------

with open(
    "data_science/reports/eda_report.txt",
    "w"
) as report:

    report.write("Retail Sales EDA Report\n\n")

    report.write(
        f"Total Records : {len(df)}\n"
    )

    report.write(
        f"Total Revenue : {df['revenue'].sum():.2f}\n"
    )

    report.write(
        f"Average Revenue : {df['revenue'].mean():.2f}\n"
    )

    report.write(
        f"Unique Products : {df['stock_code'].nunique()}\n"
    )

    report.write(
        f"Unique Customers : {df['customer_id'].nunique()}\n"
    )
    report.write(
        f"Total Profit : {df['profit'].sum()}\n"
    )

    report.write(
        f"Total Orders : {df['invoice'].nunique()}\n"
    )

    report.write(
        f"Average Order Value : {df['revenue'].sum()/df['invoice'].nunique()}\n"
    )