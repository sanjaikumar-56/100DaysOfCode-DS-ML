# Day 35 - Sorting and Ranking in Pandas

import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Asha', 'Bala', 'Kiran', 'Deepa', 'Ravi'],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'Finance'],
    'Salary': [40000, 52000, 55000, 60000, 50000],
    'Experience': [2, 5, 3, 7, 4]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# 🔹 Sort by salary (ascending)
sorted_salary_asc = df.sort_values(by='Salary')
print("\nSorted by Salary (Ascending):")
print(sorted_salary_asc)

# 🔹 Sort by salary (descending)
sorted_salary_desc = df.sort_values(by='Salary', ascending=False)
print("\nSorted by Salary (Descending):")
print(sorted_salary_desc)

# 🔹 Sort by multiple columns
sorted_multi = df.sort_values(by=['Department', 'Salary'], ascending=[True, False])
print("\nSorted by Department ASC, Salary DESC:")
print(sorted_multi)

# 🔹 Ranking by Salary
df['Salary_Rank'] = df['Salary'].rank(method='dense', ascending=False)
print("\nSalary Ranking:")
print(df)

# 🔹 Ranking by Experience
df['Experience_Rank'] = df['Experience'].rank(method='average', ascending=False)
print("\nExperience Ranking:")
print(df)
