# Day 5: Learning Lists in Python

# Create a list of fruits
fruits = ["apple", "banana", "cherry", "mango"]

# Print all fruits
print("All fruits:", fruits)

# Print first fruit
print("First fruit:", fruits[0])

# Add a new fruit
fruits.append("orange")
print("After adding:", fruits)

# Remove a fruit
fruits.remove("banana")
print("After removing banana:", fruits)

# Count how many fruits
print("Total fruits:", len(fruits))

# Loop through the list
print("Listing all fruits:")
for fruit in fruits:
    print("-", fruit)
