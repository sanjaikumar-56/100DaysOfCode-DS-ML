# Day 14: Python Dictionaries

# Creating a dictionary
student = {
    "name": "Sanjai",
    "age": 22,
    "course": "Data Science",
    "skills": ["Python", "SQL", "Power BI"]
}

# Accessing values
print("Name:", student["name"])
print("Course:", student["course"])

# Adding new key-value pair
student["grade"] = "A"

# Updating existing value
student["age"] = 23

# Removing a key-value pair
student.pop("grade")

# Looping through dictionary
for key, value in student.items():
    print(f"{key}: {value}")

# Checking if key exists
if "skills" in student:
    print("Skills:", student["skills"])

# Dictionary length
print("Total keys:", len(student))
