# Topic: String Methods
# Difficulty: Intermediate
# Goal: Look for text inside a string

text = "the quick brown fox jumps over the lazy dog"

print(text.find("quick"))        # index of the first match
print(text.find("cat"))          # -1 means NOT found
print(text.rfind("the"))         # search from the right
print(text.index("fox"))         # like find(), but crashes if missing
print(text.count("the"))         # how many times it appears
print(text.count("o"))

# Starts or ends with
filename = "report_2026.pdf"
print(filename.startswith("report"))
print(filename.endswith(".pdf"))
print(filename.endswith((".png", ".jpg")))   # a tuple checks several endings

# The "in" operator is the simplest check
print("fox" in text)
print("cat" in text)

# Practical use: find() with a start position to get the second match
first = text.find("the")
second = text.find("the", first + 1)
print(first, second)

# Expected output:
# 4
# -1
# 31
# 16
# 2
# 4
# True
# True
# False
# True
# False
# 0 31
