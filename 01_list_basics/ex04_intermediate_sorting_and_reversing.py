# Topic: List Basics
# Difficulty: Intermediate
# Goal: Sort and reverse lists, and know the difference between sort() and sorted()

numbers = [5, 2, 9, 1, 7]

# sort() changes the ORIGINAL list and returns None
numbers.sort()
print(numbers)

numbers.sort(reverse=True)         # biggest to smallest
print(numbers)

# reverse() just flips the current order (it does not sort)
letters = ["c", "a", "d", "b"]
letters.reverse()
print(letters)

# sorted() returns a NEW list and leaves the original untouched
original = [3, 1, 2]
new_list = sorted(original)
print(original)
print(new_list)

# Sorting strings is alphabetical
names = ["Cara", "ben", "Ana"]
print(sorted(names))               # capital letters come before lowercase
print(sorted(names, key=str.lower))  # ignore the case

# key= lets you choose HOW to sort. Here: by word length
words = ["banana", "kiwi", "apple", "fig"]
print(sorted(words, key=len))

# Expected output:
# [1, 2, 5, 7, 9]
# [9, 7, 5, 2, 1]
# ['b', 'd', 'a', 'c']
# [3, 1, 2]
# [1, 2, 3]
# ['Ana', 'Cara', 'ben']
# ['Ana', 'ben', 'Cara']
# ['fig', 'kiwi', 'apple', 'banana']
