# Day 17: Nested Loops and Pattern Printing in Python

# Nested loops = one loop inside another
# Used for patterns, matrices, and 2D structures.

# Example 1: Simple nested loop
print("Example 1: Nested loop demonstration")
for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")
print()

# Example 2: Square pattern
print("Example 2: Square pattern")
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()
print()

# Example 3: Right-angled triangle pattern
print("Example 3: Right-angled triangle pattern")
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()
print()

# Example 4: Inverted triangle pattern
print("Example 4: Inverted triangle pattern")
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
