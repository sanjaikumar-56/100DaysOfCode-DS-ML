# Day 31 - GroupBy and Aggregation in Pandas

import pandas as pd

# 🔹 Create sample DataFrame
data = {
    'Department': ['HR', 'IT', 'IT', 'Finance', 'HR', 'Finance', 'IT'],
    'Employee': ['Asha', 'Bala', 'Kiran', 'Deepa', 'Mani', 'Ravi', 'Kumar'],
    'Salary': [40000, 50000, 55000, 60000, 42000, 65000, 58000],
    'Experience': [2, 3, 4, 5, 2, 6, 4]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# 🔹 Group by Department and calculate mean salary
mean_salary = df.groupby('Department')['Salary'].mean()
print("\nAverage Salary by Department:")
print(mean_salary)

# 🔹 Group by Department and count employees
employee_count = df.groupby('Department')['Employee'].count()
print("\nEmployee Count by Department:")
print(employee_count)

# 🔹 Multiple aggregations
multi_agg = df.groupby('Department').agg({
    'Salary': ['mean', 'max', 'min'],
    'Experience': ['mean', 'max']
})
print("\nMultiple Aggregations by Department:")
print(multi_agg)

# 🔹 Reset index for cleaner view
multi_agg = multi_agg.reset_index()
print("\nAggregated DataFrame with Reset Index:")
print(multi_agg)
