# Day 13 - Python String Formatting (f-strings, format, %)

# Sample data
name = "Sanjai"
age = 21
course = "Data Science"

# 1️⃣ Using f-strings (modern & preferred)
print(f"My name is {name}, I am {age} years old and I study {course}.")

# You can also do calculations inside f-strings
marks = 88.5678
print(f"{name} scored {marks:.2f}% in {course}.")

# 2️⃣ Using .format() method
print("My name is {}, I am {} years old and I study {}.".format(name, age, course))
print("I scored {:.1f}% in {}".format(marks, course))

# 3
