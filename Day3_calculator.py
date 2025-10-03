# Day 3: Simple Calculator

# Ask user for two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Show options
print("Choose operation: +, -, *, /")
op = input("Enter operation: ")

# Do the calculation
if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Cannot divide by zero")
else:
    print("Invalid operation!")
