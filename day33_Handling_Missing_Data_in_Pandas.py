# Day 33 - Handling Missing Data in Pandas

import pandas as pd
import numpy as np

# 🔹 Create a sample DataFrame with missing values
data = {
    'Name': ['Asha', 'Bala', 'Kiran', 'Deepa', 'Mani'],
    'Age': [25, np.nan, 30, 28, np.nan],
    'Salary': [40000, 50000, np.nan, 55000, 48000],
    'Department': ['HR', 'IT', np.nan, 'Finance', 'IT']
}

df = pd.DataFrame(data)
print("Original DataFrame with Missing Values:")
print(df)

# 🔹 Detect missing values
print("\nCheck Missing Values:")
print(df.isnull().sum())

# 🔹 Drop rows with missing values
dropped_df = df.dropna()
print("\nAfter Dropping Rows with Missing Values:")
print(dropped_df)

# 🔹 Fill missing values with a constant
filled_constant = df.fillna("Not Available")
print("\nFilled Missing Values with 'Not Available':")
print(filled_constant)

# 🔹 Fill missing numerical values with mean
filled_mean = df.copy()
filled_mean['Age'] = filled_mean['Age'].fillna(filled_mean['Age'].mean())
filled_mean['Salary'] = filled_mean['Salary'].fillna(filled_mean['Salary'].mean())
print("\nFilled Missing Values with Mean:")
print(filled_mean)

# 🔹 Forward fill (use previous value)
ffill_df = df.fillna(method='ffill')
print("\nForward Fill:")
print(ffill_df)

# 🔹 Backward fill (use next value)
bfill_df = df.fillna(method='bfill')
print("\nBackward Fill:")
print(bfill_df)
