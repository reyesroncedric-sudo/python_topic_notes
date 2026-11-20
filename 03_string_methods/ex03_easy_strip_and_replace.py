# Topic: String Methods
# Difficulty: Easy
# Goal: Clean a string and replace parts of it

messy = "   hello world   "

print("[" + messy.strip() + "]")    # remove spaces on both sides
print("[" + messy.lstrip() + "]")   # left side only
print("[" + messy.rstrip() + "]")   # right side only

# strip() can remove other characters too
print("***sale***".strip("*"))

# replace(old, new)
sentence = "I like cats. Cats are cute."
print(sentence.replace("cats", "dogs"))     # case matters: "Cats" is untouched
print(sentence.replace("a", "@"))

# replace(old, new, count) limits the number of changes
print("aaaa".replace("a", "b", 2))

# Remove something by replacing it with nothing
phone = "555-123-4567"
print(phone.replace("-", ""))

# Expected output:
# [hello world]
# [hello world   ]
# [   hello world]
# sale
# I like dogs. Cats are cute.
# I like c@ts. C@ts @re cute.
# bbaa
# 5551234567
