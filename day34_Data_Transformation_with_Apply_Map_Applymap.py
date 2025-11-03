# Day 34 - Data Transformation with Apply, Map, and Applymap in Pandas

import pandas as pd

# 🔹 Create a sample DataFrame
data = {
    'Name': ['Asha', 'Bala', 'Kiran', 'Deepa'],
    'Department': ['HR', 'IT', 'Finance', 'IT'],
    'Salary': [40000, 50000, 55000, 60000]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# 🔹 Using map() - works on Series (single column)
df['Department'] = df['Department'].map({'HR': 'Human Resources', 'IT': 'Information Tech', 'Finance': 'Accounts'})
print("\nAfter map() transformation:")
print(df)

# 🔹 Using apply() - works on Series or DataFrame axis
df['Bonus'] = df['Salary'].apply(lambda x: x * 0.10)
print("\nAfter apply() to calculate Bonus:")
print(df)

# 🔹 Using applymap() - works element-wise on entire DataFrame
numeric_df = df[['Salary', 'Bonus']]
print("\nNumeric Columns:")
print(numeric_df)

transformed_df = numeric_df.applymap(lambda x: round(x / 1000, 1))
print("\nAfter applymap() transformation (values in thousands):")
print(transformed_df)
