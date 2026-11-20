# Topic: List Basics
# Difficulty: Intermediate
# Goal: Understand copying lists and working with lists inside lists

# --- Alias: two names for the SAME list ---
a = [1, 2, 3]
b = a
b.append(4)
print(a)               # a changed too!
print(a is b)          # True: same object

# --- Copy: a separate list ---
c = a.copy()           # also: list(a) or a[:]
c.append(99)
print(a)               # a did not change
print(c)
print(a is c)          # False

# --- Nested lists (a list inside a list) ---
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(matrix[0])       # first row
print(matrix[1][2])    # row 1, column 2
matrix[2][0] = 70      # change one value
print(matrix)

# Loop through every value
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()            # new line after each row

# Expected output:
# [1, 2, 3, 4]
# True
# [1, 2, 3, 4]
# [1, 2, 3, 4, 99]
# False
# [1, 2, 3]
# 6
# [[1, 2, 3], [4, 5, 6], [70, 8, 9]]
# 1 2 3
# 4 5 6
# 70 8 9
