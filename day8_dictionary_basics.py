# Day 8: Learning Dictionaries in Python

# Creating a dictionary
student = {
    "name": "Sanjai",
    "age": 21,
    "course": "Data Science",
    "marks": 88
}

# Print the whole dictionary
print("Student Dictionary:", student)

# Access values using keys
print("Name:", student["name"])
print("Course:", student["course"])

# Add a new key-value pair
student["city"] = "Coimbatore"
print("After adding city:", student)

# Change a value
student["marks"] = 92
print("After updating marks:", student)

# Remove a key
student.pop("age")
print("After removing age:", student)

# Loop through the dictionary
print("\nAll student details:")
for key, value in student.items():
    print(key, ":", value)
