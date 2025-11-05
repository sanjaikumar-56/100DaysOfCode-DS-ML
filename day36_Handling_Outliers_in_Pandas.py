# Day 36 - Handling Outliers in Pandas

import pandas as pd
import numpy as np

# Sample Data with Outliers
data = {
    'Employee': ['Asha', 'Bala', 'Kiran', 'Deepa', 'Ravi', 'Mani', 'Arjun'],
    'Salary': [40000, 42000, 45000, 50000, 52000, 800000, 48000]  # 800000 is an outlier
}

df = pd.DataFrame(data)
print("Original Data:")
print(df)

# ---------- Method 1: Detect outliers using IQR ----------
Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)
IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 - 1.5 * IQR  # Correction after reading typical method

upper_limit = Q3 + 1.5 * IQR  # correct upper limit line

print("\nIQR Outlier Range:")
print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)

# Filter outliers
outliers = df[(df['Salary'] < lower_limit) | (df['Salary'] > upper_limit)]
print("\nDetected Outliers:")
print(outliers)

# Remove outliers
df_no_outliers = df[(df['Salary'] >= lower_limit) & (df['Salary'] <= upper_limit)]
print("\nData after Removing Outliers:")
print(df_no_outliers)

# ---------- Method 2: Capping Outliers (Winsorization) ----------
df_capped = df.copy()
df_capped['Salary'] = np.where(df['Salary'] > upper_limit, upper_limit,
                               np.where(df['Salary'] < lower_limit, lower_limit, df['Salary']))

print("\nAfter Capping Outliers (Winsorization):")
print(df_capped)
