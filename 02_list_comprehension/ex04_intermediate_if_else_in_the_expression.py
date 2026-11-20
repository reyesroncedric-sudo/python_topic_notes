# Topic: List Comprehension
# Difficulty: Intermediate
# Goal: Choose between two results for every element (if-else)

# Remember the two positions of "if":
#   [x for x in data if condition]          -> FILTER (some items are dropped)
#   [A if condition else B for x in data]   -> CHOOSE (every item is kept)

numbers = [1, 2, 3, 4, 5]
labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
print(labels)

# Pass or fail labels
scores = [35, 60, 85, 45, 90]
results = ["Pass" if s >= 50 else "Fail" for s in scores]
print(results)

# Replace negative numbers with 0
data = [4, -2, 7, -9, 3]
cleaned = [n if n >= 0 else 0 for n in data]
print(cleaned)

# Three choices: chain the conditions
grades = ["A" if s >= 85 else "B" if s >= 50 else "F" for s in scores]
print(grades)

# Compare with the filter version: here the failing scores disappear
only_passed = [s for s in scores if s >= 50]
print(only_passed)

# Expected output:
# ['odd', 'even', 'odd', 'even', 'odd']
# ['Fail', 'Pass', 'Pass', 'Fail', 'Pass']
# [4, 0, 7, 0, 3]
# ['F', 'B', 'A', 'F', 'A']
# [60, 85, 90]
