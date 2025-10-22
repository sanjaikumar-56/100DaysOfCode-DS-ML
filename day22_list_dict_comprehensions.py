# Day 22: Python List and Dictionary Comprehensions

# 1️⃣ List Comprehension Basics
numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers]
print("Squares using list comprehension:", squares)
print()

# 2️⃣ Adding a condition inside list comprehension
even_squares = [x ** 2 for x in numbers if x % 2 == 0]
print("Even squares using condition:", even_squares)
print()

# 3️⃣ Nested list comprehension
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]
print("Flattened list from matrix:", flattened)
print()

# 4️⃣ Dictionary Comprehension
students = ["Sanjai", "Kumar", "John"]
marks = [88, 92, 79]
student_dict = {students[i]: marks[i] for i in range(len(students))}
print("Dictionary using comprehension:", student_dict)
print()

# 5️⃣ Conditional Dictionary Comprehension
passed_students = {name: mark for name, mark in zip(students, marks) if mark >= 85}
print("Passed students:", passed_students)
