# Topic: List Basics
# Difficulty: Intermediate
# Goal: Search a list and calculate with built-in functions

grades = [88, 92, 79, 95, 92, 70]

# Searching
print(92 in grades)           # membership test -> True/False
print(100 in grades)
print(grades.index(79))       # position of the first match
print(grades.count(92))       # how many times it appears

# Math with built-in functions
print(len(grades))
print(sum(grades))
print(min(grades))
print(max(grades))
average = sum(grades) / len(grades)
print(round(average, 2))

# Practical example: find the position of the highest grade
highest = max(grades)
print("Highest:", highest, "at index", grades.index(highest))

# index() crashes if the value is missing, so check first
target = 50
if target in grades:
    print("Found at", grades.index(target))
else:
    print(target, "is not in the list")

# Expected output:
# True
# False
# 2
# 2
# 6
# 516
# 70
# 95
# 86.0
# Highest: 95 at index 3
# 50 is not in the list
