# Day 6: Learning Functions in Python

# Define a function
def greet(name):
    print("Hello,", name, "! Welcome to Python functions!")

# Define a function to add two numbers
def add_numbers(a, b):
    return a + b  # 'return' gives back the result

# Define a function to check even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# --- Calling (using) the functions ---
greet("Sanjai")

sum_result = add_numbers(5, 10)
print("Sum of 5 and 10 is:", sum_result)

print("7 is", check_even_odd(7))
print("12 is", check_even_odd(12))
