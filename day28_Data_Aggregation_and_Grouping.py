# Day 28 - Data Aggregation and Grouping in Pandas

import pandas as pd

# Sample dataset
data = {
    'Region': ['North', 'South', 'East', 'West', 'North', 'East', 'South', 'West'],
    'Product': ['A', 'A', 'B', 'B', 'C', 'C', 'A', 'B'],
    'Sales': [250, 180, 300, 200, 400, 350, 270, 150],
    'Profit': [40, 30, 50, 25, 60, 45, 35, 20]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# 🔹 Group by Region and calculate sum of Sales and Profit
region_summary = df.groupby('Region')[['Sales', 'Profit']].sum().reset_index()
print("\nTotal Sales and Profit by Region:")
print(region_summary)

# 🔹 Group by Product and calculate average Sales
product_avg = df.groupby('Product')['Sales'].mean().reset_index()
print("\nAverage Sales by Product:")
print(product_avg)

# 🔹 Multiple aggregations for Region
multi_agg = df.groupby('Region').agg({'Sales': ['sum', 'mean'], 'Profit': ['sum', 'mean']}).reset_index()
print("\nMultiple Aggregations by Region:")
print(multi_agg)

# 🔹 Using transform to add normalized sales column
df['Normalized_Sales'] = df['Sales'] / df['Sales'].max()
print("\nDataFrame with Normalized Sales:")
print(df)
