# Topic: List Comprehension
# Difficulty: Intermediate
# Goal: Use comprehensions with strings, enumerate() and zip()

# Convert text digits into integers
digits = [int(d) for d in "12345"]
print(digits)

# Keep only the vowels of a word
vowels = [c for c in "programming" if c in "aeiou"]
print(vowels)

# Clean messy names: strip spaces and fix capitalization
raw_names = ["  alice ", "BOB", " cArA  "]
clean_names = [name.strip().title() for name in raw_names]
print(clean_names)

# enumerate() gives the position and the value
names = ["Ana", "Ben", "Cara"]
numbered = [f"{i}. {name}" for i, name in enumerate(names, start=1)]
print(numbered)

# zip() walks through two lists together
prices = [10, 20, 30]
quantities = [2, 1, 3]
totals = [p * q for p, q in zip(prices, quantities)]
print(totals)

# Split a sentence and get the length of each word
sentence = "list comprehension is neat"
word_lengths = [len(word) for word in sentence.split()]
print(word_lengths)

# Expected output:
# [1, 2, 3, 4, 5]
# ['o', 'a', 'i']
# ['Alice', 'Bob', 'Cara']
# ['1. Ana', '2. Ben', '3. Cara']
# [20, 20, 90]
# [4, 13, 2, 4]
