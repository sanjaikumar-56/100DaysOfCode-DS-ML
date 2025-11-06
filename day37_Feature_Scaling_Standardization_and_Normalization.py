# Day 37 - Feature Scaling: Standardization and Normalization

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# 🔹 Create a sample dataset
data = {
    'Employee': ['Asha', 'Bala', 'Kiran', 'Deepa', 'Ravi'],
    'Experience': [2, 5, 3, 8, 4],
    'Salary': [40000, 55000, 48000, 80000, 60000]
}

df = pd.DataFrame(data)
print("Original Data:")
print(df)

# Extract numeric columns
numeric_df = df[['Experience', 'Salary']]

# ---------- Standardization ----------
# Formula: z = (x - mean) / std
scaler_standard = StandardScaler()
standardized = scaler_standard.fit_transform(numeric_df)
df_standardized = pd.DataFrame(standardized, columns=['Experience_Std', 'Salary_Std'])
print("\nAfter Standardization (Z-score scaling):")
print(df_standardized)

# ---------- Normalization ----------
# Formula: (x - min) / (max - min)
scaler_minmax = MinMaxScaler()
normalized = scaler_minmax.fit_transform(numeric_df)
df_normalized = pd.DataFrame(normalized, columns=['Experience_Norm', 'Salary_Norm'])
print("\nAfter Normalization (Min-Max scaling):")
print(df_normalized)

# Combine results with original data
df_final = pd.concat([df, df_standardized, df_normalized], axis=1)
print("\nFinal Scaled DataFrame:")
print(df_final)
