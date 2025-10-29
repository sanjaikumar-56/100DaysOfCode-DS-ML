# Day 29 - Data Merging and Joining in Pandas

import pandas as pd

# 🔹 Create sample DataFrames
sales = {
    'OrderID': [1, 2, 3, 4],
    'CustomerID': [101, 102, 103, 104],
    'Amount': [250, 400, 150, 300]
}

customers = {
    'CustomerID': [101, 102, 103, 105],
    'CustomerName': ['John', 'Alice', 'Bob', 'Emma'],
    'Region': ['North', 'East', 'South', 'West']
}

df_sales = pd.DataFrame(sales)
df_customers = pd.DataFrame(customers)

print("Sales DataFrame:")
print(df_sales)

print("\nCustomers DataFrame:")
print(df_customers)

# 🔹 Inner Join
inner_join = pd.merge(df_sales, df_customers, on='CustomerID', how='inner')
print("\nInner Join Result:")
print(inner_join)

# 🔹 Left Join
left_join = pd.merge(df_sales, df_customers, on='CustomerID', how='left')
print("\nLeft Join Result:")
print(left_join)

# 🔹 Right Join
right_join = pd.merge(df_sales, df_customers, on='CustomerID', how='right')
print("\nRight Join Result:")
print(right_join)

# 🔹 Outer Join
outer_join = pd.merge(df_sales, df_customers, on='CustomerID', how='outer')
print("\nOuter Join Result:")
print(outer_join)
