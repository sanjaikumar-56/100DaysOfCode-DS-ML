# Day 38 - Encoding Categorical Variables (LabelEncoder and OneHotEncoder)

import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# 🔹 Create a sample dataset
data = {
    'Name': ['Asha', 'Bala', 'Kiran', 'Deepa', 'Ravi'],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'Experience_Level': ['Junior', 'Senior', 'Mid', 'Senior', 'Junior']
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# ---------- Label Encoding ----------
# Converts categories into numeric codes (0,1,2,...)
le = LabelEncoder()
df['Dept_Label'] = le.fit_transform(df['Department'])
df['Exp_Label'] = le.fit_transform(df['Experience_Level'])

print("\nAfter Label Encoding:")
print(df)

# ---------- One-Hot Encoding ----------
# Converts each category into a binary column (0/1)
ohe = OneHotEncoder(sparse_output=False)
encoded_data = ohe.fit_transform(df[['Department']])

# Create a DataFrame for one-hot encoded data
ohe_df = pd.DataFrame(encoded_data, columns=ohe.get_feature_names_out(['Department']))
df_encoded = pd.concat([df, ohe_df], axis=1)

print("\nAfter One-Hot Encoding:")
print(df_encoded)
