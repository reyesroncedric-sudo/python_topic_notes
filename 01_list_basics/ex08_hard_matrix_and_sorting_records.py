# Topic: List Basics
# Difficulty: Hard
# Goal: Process a 2D list (matrix) and sort a list of records

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# 1) Sum of each row
for row in matrix:
    print("Row sum:", sum(row))

# 2) Sum of each column
for col in range(3):
    column_total = 0
    for row in matrix:
        column_total += row[col]
    print("Column", col, "sum:", column_total)

# 3) Main diagonal (top-left to bottom-right)
diagonal = []
for i in range(3):
    diagonal.append(matrix[i][i])
print("Diagonal:", diagonal)

# 4) Transpose: rows become columns
transposed = []
for col in range(3):
    new_row = []
    for row in matrix:
        new_row.append(row[col])
    transposed.append(new_row)
print(transposed)

# 5) Sort a list of records [name, score] by score, highest first
students = [["Ana", 85], ["Ben", 92], ["Cara", 78], ["Dan", 92]]
students.sort(key=lambda student: student[1], reverse=True)
print(students)

# 6) Top 3 names
top3 = [student[0] for student in students[:3]]
print("Top 3:", top3)

# Expected output:
# Row sum: 6
# Row sum: 15
# Row sum: 24
# Column 0 sum: 12
# Column 1 sum: 15
# Column 2 sum: 18
# Diagonal: [1, 5, 9]
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
# [['Ben', 92], ['Dan', 92], ['Ana', 85], ['Cara', 78]]
# Top 3: ['Ben', 'Dan', 'Ana']
