import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("sales_data.csv")

# Create total sales column
df["Sales"] = df["Units"] * df["Unit_Price"]

# Group sales data
region_sales = df.groupby("Region")["Sales"].sum()
product_sales = df.groupby("Product")["Sales"].sum()

# Print insights
print("\nTotal Sales: $", df["Sales"].sum())
print("\nSales by Region:\n", region_sales)
print("\nSales by Product:\n", product_sales)

# Create charts
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

region_sales.plot(kind="bar", color="skyblue", ax=axes[0])
axes[0].set_title("Sales by Region")
axes[0].set_ylabel("Sales ($)")

product_sales.plot(kind="bar", color="lightgreen", ax=axes[1])
axes[1].set_title("Sales by Product")
axes[1].set_ylabel("Sales ($)")

plt.tight_layout()
plt.show()