# Day 20: Python Functions (Part 2 - Argument Types)
# Types of arguments: positional, keyword, *args, and **kwargs

# 1️⃣ Positional Arguments - order matters
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet("Sanjai", 21)
print()

# 2️⃣ Keyword Arguments - order doesn’t matter
greet(age=25, name="Kumar")
print()

# 3️⃣ Default Arguments - used when a value is not passed
def welcome(name="Sanjai", country="India"):
    print(f"Welcome {name} from {country}!")

welcome()
welcome("John", "USA")
print()

# 4️⃣ Variable-length Arguments (*args)
def add_numbers(*args):
    total = sum(args)
    print("Sum of numbers:", total)

add_numbers(2, 4, 6, 8)
print()

# 5️⃣ Keyword Variable-length Arguments (**kwargs)
def print_details(**kwargs):
    print("User Details:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(Name="Sanjai", Age=21, City="Coimbatore", Course="Data Science")
