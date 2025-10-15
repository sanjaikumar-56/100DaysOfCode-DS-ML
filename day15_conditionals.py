# Day 15: Python Conditional Statements (if, elif, else)

# Conditional statements help make decisions in programs.

# Example: Checking temperature
temperature = 28

if temperature > 30:
    print("It's a hot day 🌞")
elif temperature > 20:
    print("It's a pleasant day 🌤️")
elif temperature > 10:
    print("It's a bit cold 🧥")
else:
    print("It's cold ❄️")

# Example: Checking user input
age = 18

if age >= 18:
    print("You are eligible to vote 🗳️")
else:
    print("You are not eligible to vote 🚫")

# Using nested if
num = -5

if num >= 0:
    if num == 0:
        print("Number is zero")
    else:
        print("Number is positive")
else:
    print("Number is negative")
