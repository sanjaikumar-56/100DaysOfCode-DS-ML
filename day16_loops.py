# Day 16: Python Loops (for and while)

# Loops are used to repeat a block of code multiple times.

# Example 1: For loop with a range
print("For Loop Example:")
for i in range(1, 6):
    print("Number:", i)

# Example 2: Loop through a list
fruits = ["apple", "banana", "cherry"]
print("\nLoop through a list:")
for fruit in fruits:
    print(fruit)

# Example 3: While loop
print("\nWhile Loop Example:")
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1

# Example 4: Break and continue
print("\nBreak and Continue Example:")
for num in range(1, 10):
    if num == 5:
        print("Skipping number 5 using continue")
        continue
    if num == 8:
        print("Breaking the loop at number 8")
        break
    print("Number:", num)
