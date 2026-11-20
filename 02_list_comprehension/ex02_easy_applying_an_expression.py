# Topic: List Comprehension
# Difficulty: Easy
# Goal: Change every element with an expression

# The expression is the part BEFORE the word "for"
squares = [x ** 2 for x in range(1, 6)]
print(squares)

# Use it with an existing list
numbers = [2, 4, 6, 8]
double = [n * 2 for n in numbers]
print(double)

# Works with strings too
fruits = ["apple", "banana", "orange"]
uppercase = [fruit.upper() for fruit in fruits]
print(uppercase)

lengths = [len(fruit) for fruit in fruits]
print(lengths)

# A string is iterable, so you can split it into letters
letters = [letter for letter in "Python"]
print(letters)

# The original list is NOT changed: a NEW list is created
print(numbers)

# Expected output:
# [1, 4, 9, 16, 25]
# [4, 8, 12, 16]
# ['APPLE', 'BANANA', 'ORANGE']
# [5, 6, 6]
# ['P', 'y', 't', 'h', 'o', 'n']
# [2, 4, 6, 8]
