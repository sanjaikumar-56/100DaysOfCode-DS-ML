# Day 32 - Merging and Joining DataFrames in Pandas

import pandas as pd

# 🔹 Create two sample DataFrames
employees = pd.DataFrame({
    'EmpID': [101, 102, 103, 104],
    'Name': ['Asha', 'Bala', 'Kiran', 'Deepa'],
    'DeptID': [1, 2, 2, 3]
})

departments = pd.DataFrame({
    'DeptID': [1, 2, 3, 4],
    'Department': ['HR', 'IT', 'Finance', 'Marketing']
})

print("Employees DataFrame:")
print(employees)

print("\nDepartments DataFrame:")
print(departments)

# 🔹 Inner Join (only matching DeptID)
inner_join = pd.merge(employees, departments, on='DeptID', how='inner')
print("\nInner Join Result:")
print(inner_join)

# 🔹 Left Join (all employees, even if DeptID missing)
left_join = pd.merge(employees, departments, on='DeptID', how='left')
print("\nLeft Join Result:")
print(left_join)

# 🔹 Right Join (all departments, even if no employee)
right_join = pd.merge(employees, departments, on='DeptID', how='right')
print("\nRight Join Result:")
print(right_join)

# 🔹 Outer Join (all records from both tables)
outer_join = pd.merge(employees, departments, on='DeptID', how='outer')
print("\nOuter Join Result:")
print(outer_join)
