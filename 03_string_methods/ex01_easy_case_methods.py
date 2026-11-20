# Topic: String Methods
# Difficulty: Easy
# Goal: Change the capitalization of a string

message = "hello python world"

print(message.upper())        # all capitals
print(message.lower())        # all small letters
print(message.title())        # first letter of EACH word
print(message.capitalize())   # first letter of the whole string only
print("Hello".swapcase())     # swap upper and lower

# Strings are immutable: the original is never changed
print(message)

# Save the result in a variable to keep it
loud = message.upper()
print(loud)

# Check the case
print("HELLO".isupper())
print("hello".islower())
print("Hello World".istitle())

# Expected output:
# HELLO PYTHON WORLD
# hello python world
# Hello Python World
# Hello python world
# hELLO
# hello python world
# HELLO PYTHON WORLD
# True
# True
# True
