# Topic: String Methods
# Difficulty: Easy
# Goal: Measure a string and pick out characters

word = "Programming"
#  index: 0 1 2 3 4 5 6 7 8 9 10

print(len(word))        # number of characters
print(word[0])          # first character
print(word[-1])         # last character
print(word[0:3])        # "Pro" (stop index is not included)
print(word[3:])         # from index 3 to the end
print(word[:4])         # first four characters
print(word[::-1])       # reversed string

# Loop through the characters
for letter in "Hi!":
    print(letter)

# Strings cannot be changed by index: word[0] = "p" would give an error.
# Build a new string instead
new_word = "p" + word[1:]
print(new_word)

# Expected output:
# 11
# P
# g
# Pro
# gramming
# Prog
# gnimmargorP
# H
# i
# !
# programming
