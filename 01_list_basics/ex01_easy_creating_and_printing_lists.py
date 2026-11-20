# Topic: List Basics
# Difficulty: Easy
# Goal: Create lists and print them

# A list holds many values in one variable. Use square brackets [ ] and commas.
fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40]
mixed = ["Ana", 21, True, 3.5]    # a list can hold different data types
empty = []                        # an empty list

print(fruits)
print(numbers)
print(mixed)
print(empty)

print(type(fruits))               # the type is list
print(len(fruits))                # len() counts the items

# list() can build a list from other things
letters = list("abc")
evens = list(range(0, 11, 2))     # 0, 2, 4, ... 10
print(letters)
print(evens)

# Loop through a list with for-in
for fruit in fruits:
    print("I like", fruit)

# Expected output:
# ['apple', 'banana', 'cherry']
# [10, 20, 30, 40]
# ['Ana', 21, True, 3.5]
# []
# <class 'list'>
# 3
# ['a', 'b', 'c']
# [0, 2, 4, 6, 8, 10]
# I like apple
# I like banana
# I like cherry
