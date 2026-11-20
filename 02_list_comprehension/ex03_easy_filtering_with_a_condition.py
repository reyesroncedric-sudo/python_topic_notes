# Topic: List Comprehension
# Difficulty: Easy
# Goal: Keep only the elements that pass a test

# Syntax:  [expression for item in iterable if condition]

# Even numbers
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)

# Passing scores (50 or higher)
scores = [35, 60, 85, 45, 90]
passed = [score for score in scores if score >= 50]
print(passed)

# Numbers greater than 50
values = [12, 55, 73, 8, 61]
big = [v for v in values if v > 50]
print(big)

# Words that start with "b"
words = ["bat", "cat", "ball", "dog", "bird"]
b_words = [w for w in words if w.startswith("b")]
print(b_words)

# Filter AND change at the same time: squares of odd numbers
odd_squares = [n ** 2 for n in range(1, 10) if n % 2 != 0]
print(odd_squares)

# Expected output:
# [2, 4, 6, 8, 10]
# [60, 85, 90]
# [55, 73, 61]
# ['bat', 'ball', 'bird']
# [1, 9, 25, 49, 81]
