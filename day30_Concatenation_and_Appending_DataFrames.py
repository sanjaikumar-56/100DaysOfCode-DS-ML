# Day 30 - Concatenation and Appending DataFrames in Pandas

import pandas as pd

# 🔹 Create sample DataFrames
data1 = {
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Marks': [85, 90, 88]
}

data2 = {
    'ID': [4, 5, 6],
    'Name': ['David', 'Emma', 'Frank'],
    'Marks': [75, 80, 95]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print("DataFrame 1:")
print(df1)

print("\nDataFrame 2:")
print(df2)

# 🔹 Concatenating DataFrames (stacking rows)
concat_df = pd.concat([df1, df2], ignore_index=True)
print("\nConcatenated DataFrame (Row-wise):")
print(concat_df)

# 🔹 Concatenating column-wise
extra_data = pd.DataFrame({
    'Subject': ['Math', 'Science', 'English', 'Math', 'Science', 'English']
})
concat_col = pd.concat([concat_df, extra_data], axis=1)
print("\nConcatenated DataFrame (Column-wise):")
print(concat_col)

# 🔹 Appending a single row
new_row = {'ID': 7, 'Name': 'Grace', 'Marks': 89, 'Subject': 'Physics'}
appended_df = pd.concat([concat_col, pd.DataFrame([new_row])], ignore_index=True)
print("\nAfter Appending New Row:")
print(appended_df)
