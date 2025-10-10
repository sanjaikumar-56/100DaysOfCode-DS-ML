# Day 10 - Learning Python Sets

# Creating a set
numbers = {1, 2, 3, 4, 4, 5}
print("Original Set:", numbers)  # Duplicates removed automatically

# Adding items
numbers.add(6)
print("After adding 6:", numbers)

# Removing items
numbers.remove(3)
print("After removing 3:", numbers)

# Checking membership
print("Is 2 in the set?", 2 in numbers)
print("Is 10 in the set?", 10 in numbers)

# Set operations
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}

print("\nUnion:", setA | setB)         # All unique items
print("Intersection:", setA & setB)   # Common items
print("Difference (A - B):", setA - setB)
print("Symmetric Difference:", setA ^ setB)  # Items not common in both

# Clearing the set
numbers.clear()
print("\nAfter clearing:", numbers)
