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

# df["Revenue"] = df["quantity"]*df["price"]
# print(df["Revenue"].sum())

