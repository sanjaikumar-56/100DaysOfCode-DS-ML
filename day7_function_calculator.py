# Day 7: Calculator Using Functions

# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide two numbers
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Cannot divide by zero!"

# --- Main Program ---
print("Welcome to Function Calculator!")
print("Choose operation: +, -, *, /")

op = input("Enter operation: ")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Using functions for each operation
if op == "+":
    print("Result:", add(a, b))
elif op == "-":
    print("Result:", subtract(a, b))
elif op == "*":
    print("Result:", multiply(a, b))
elif op == "/":
    print("Result:", divide(a, b))
else:
    print("Invalid operation!")
