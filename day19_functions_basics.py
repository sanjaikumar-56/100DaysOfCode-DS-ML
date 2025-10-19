# Day 19: Python Functions (Basics & Parameters)

# Functions help us organize code into reusable blocks.

# 1️⃣ Defining a simple function
def greet():
    print("Hello, Sanjai! Welcome to Day 19 of your coding journey!")

# Calling the function
greet()
print()

# 2️⃣ Function with parameters
def add_numbers(a, b):
    result = a + b
    print(f"The sum of {a} and {b} is {result}")

add_numbers(5, 7)
print()

# 3️⃣ Function with return statement
def multiply(x, y):
    return x * y

product = multiply(4, 6)
print("The product is:", product)
print()

# 4️⃣ Function with default parameter
def introduce(name="Sanjai"):
    print(f"Hi, my name is {name}.")

introduce()
introduce("Kumar")
