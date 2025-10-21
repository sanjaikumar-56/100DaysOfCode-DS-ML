# Day 21: Lambda Functions and Map, Filter, Reduce in Python

# Lambda functions are small, one-line anonymous functions.
# Syntax: lambda arguments: expression

# 1️⃣ Basic lambda function
add = lambda a, b: a + b
print("Sum using lambda:", add(5, 7))
print()

# 2️⃣ Lambda with map() - applies a function to each item
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print("Squared numbers using map:", squared)
print()

# 3️⃣ Lambda with filter() - filters elements based on condition
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using filter:", even_numbers)
print()

# 4️⃣ Lambda with reduce() - combines all elements into a single value
from functools import reduce

product = reduce(lambda x, y: x * y, numbers)
print("Product of all numbers using reduce:", product)
print()

# 5️⃣ Combining map, filter, and lambda
filtered_squared = list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, numbers)))
print("Squares of odd numbers:", filtered_squared)
