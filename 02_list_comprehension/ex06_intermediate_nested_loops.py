# Topic: List Comprehension
# Difficulty: Intermediate
# Goal: Use two for-clauses in one comprehension

# The clauses are read in the SAME order as nested for loops.

# Traditional nested loops
pairs = []
for x in [1, 2]:
    for y in ["a", "b"]:
        pairs.append((x, y))
print(pairs)

# Same thing as a comprehension
pairs = [(x, y) for x in [1, 2] for y in ["a", "b"]]
print(pairs)

# Flatten a 2D list into a 1D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [value for row in matrix for value in row]
print(flat)

# Add a condition: only the even values
even_flat = [value for row in matrix for value in row if value % 2 == 0]
print(even_flat)

# Pairs with different values only
different = [(a, b) for a in [1, 2, 3] for b in [1, 2, 3] if a != b]
print(different)

# One row of a multiplication table
table_of_7 = [7 * i for i in range(1, 11)]
print(table_of_7)

# Expected output:
# [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
# [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [2, 4, 6, 8]
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
# [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
