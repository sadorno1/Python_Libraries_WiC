import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the CSV file
df = pd.read_csv("sales.csv", parse_dates=["date"])

# 2. Preview and basic stats
print("=== Preview ===")
print(df.head())

print("\n=== Summary Statistics ===")
df.select_dtypes(include="number").describe()

# 3. Group and aggregate (sales by region)
grouped = df.groupby("region")["sales"].sum()
print("\n=== Total Sales by Region ===")
print(grouped)

# 4. Plot the bar chart
plt.figure(figsize=(6, 4))
grouped.plot(kind="bar", color=["#66b3ff", "#99ff99", "#ffcc99"])
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.savefig("sales_by_region.png", dpi=150)
plt.show()

# MINI CHALLENGE 
# Instead of plotting sales by region,
# try plotting total sales by date (x-axis = date, y-axis = total sales).
# Hint: group by the "date" column instead of "region" and plot a line chart.



















