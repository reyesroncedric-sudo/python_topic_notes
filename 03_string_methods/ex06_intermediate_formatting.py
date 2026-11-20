# Topic: String Methods
# Difficulty: Intermediate
# Goal: Format text so it looks neat

name = "Ana"
score = 92.4567
items = 3

# f-strings (the modern way)
print(f"{name} scored {score}")
print(f"{name} scored {score:.1f}")          # 1 decimal place
print(f"Total: {1234567:,}")                 # thousands separator
print(f"Passed: {85 / 100:.0%}")             # percentage

# Alignment: width of 10 characters
print("[" + "left".ljust(10) + "]")
print("[" + "right".rjust(10) + "]")
print("[" + "mid".center(10, "*") + "]")

# zfill() pads numbers with zeros
print("7".zfill(3))
print("42".zfill(5))

# format() method (older style)
print("{} has {} items".format(name, items))

# A small table using f-string alignment
print(f"{'Item':<8}{'Price':>8}")
print(f"{'Pen':<8}{1.5:>8.2f}")
print(f"{'Notebook':<8}{12.25:>8.2f}")

# Expected output:
# Ana scored 92.4567
# Ana scored 92.5
# Total: 1,234,567
# Passed: 85%
# [left      ]
# [     right]
# [***mid****]
# 007
# 00042
# Ana has 3 items
# Item       Price
# Pen         1.50
# Notebook   12.25
