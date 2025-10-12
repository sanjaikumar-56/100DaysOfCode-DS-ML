# Day 12 - Python Strings (Basics & Methods)

# Creating strings
name = "Sanjai Kumar"
greeting = 'Welcome to Python!'

# Printing strings
print("Name:", name)
print("Greeting:", greeting)

# Indexing and slicing
print("First letter:", name[0])
print("Last letter:", name[-1])
print("First 6 letters:", name[:6])
print("Reversed name:", name[::-1])

# String concatenation
full_greeting = name + " - " + greeting
print("Concatenated String:", full_greeting)

# String methods
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Replace Kumar → K:", name.replace("Kumar", "K"))
print("Count of 'a':", name.count('a'))
print("Does name start with 'San'? ->", name.startswith("San"))
print("Split by space:", name.split(" "))

# Joining list of words into string
words = ["Python", "is", "awesome"]
joined = " ".join(words)
print("Joined String:", joined)

# Finding substring
print("Position of 'Python':", greeting.find("Python"))
