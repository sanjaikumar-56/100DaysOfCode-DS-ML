# Day 11 - Python Sets

# A set is an unordered collection of unique elements
# It automatically removes duplicates

# Creating a set
fruits = {"apple", "banana", "cherry", "apple"}
print("Fruits set:", fruits)  # Duplicate 'apple' is removed

# Adding elements
fruits.add("orange")
print("After adding orange:", fruits)

# Removing elements
fruits.remove("banana")
print("After removing banana:", fruits)

# Set operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union:", A | B)          # All unique elements from both
print("Intersection:", A & B)   # Common elements
print("Difference:", A - B)     # Elements in A not in B
print("Symmetric Difference:", A ^ B)  # Elements not common to both

# Checking membership
print("Is 2 in A?", 2 in A)
print("Is 5 not in A?", 5 not in A)

# Frozen Set (immutable set)
frozen = frozenset([1, 2, 3, 3, 4])
print("Frozen set:", frozen)
