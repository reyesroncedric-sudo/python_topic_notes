# Topic: List Comprehension
# Difficulty: Hard
# Goal: Build a list of lists (a matrix) using a comprehension inside a comprehension

# The INNER comprehension builds one row; the OUTER one collects the rows.

# 1) Create a 3x3 grid
grid = [[row * 3 + col for col in range(3)] for row in range(3)]
print(grid)

# 2) Identity matrix (1 on the diagonal, 0 elsewhere)
identity = [[1 if r == c else 0 for c in range(4)] for r in range(4)]
for row in identity:
    print(row)

# 3) Transpose a matrix (rows become columns)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(3)]
print(transposed)

# 4) Apply an operation to every value inside a nested list
squared = [[value ** 2 for value in row] for row in matrix]
print(squared)

# 5) Keep only the rows whose sum is greater than 10
big_rows = [row for row in matrix if sum(row) > 10]
print(big_rows)

# 6) Largest value of each row
row_max = [max(row) for row in matrix]
print(row_max)

# Expected output:
# [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
# [1, 0, 0, 0]
# [0, 1, 0, 0]
# [0, 0, 1, 0]
# [0, 0, 0, 1]
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
# [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
# [[4, 5, 6], [7, 8, 9]]
# [3, 6, 9]
