# Day 18: Loop Control Statements in Python
# Keywords: break, continue, pass

# 1️⃣ break - stop the loop immediately
print("Example 1: Using break")
for i in range(1, 10):
    if i == 5:
        print("Loop stopped at i =", i)
        break
    print(i)
print()

# 2️⃣ continue - skip the current iteration
print("Example 2: Using continue")
for i in range(1, 8):
    if i == 4:
        print("Skipping number 4")
        continue
    print(i)
print()

# 3️⃣ pass - do nothing (used as a placeholder)
print("Example 3: Using pass")
for i in range(1, 6):
    if i == 3:
        pass  # No action performed here
    else:
        print("Number:", i)
print("\nLoop finished!")
