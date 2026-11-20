# Topic: String Methods
# Difficulty: Intermediate
# Goal: Break a string into a list, join it back, and validate its content

# split(): string -> list
csv_line = "Ana,21,Manila"
print(csv_line.split(","))

sentence = "  Python   is   fun  "
print(sentence.split())            # no argument: splits on any spaces
print(len(sentence.split()))       # word count

print("a-b-c-d".split("-", 2))     # at most 2 splits

# join(): list -> string  (the separator goes BEFORE .join)
words = ["Learn", "Python", "today"]
print(" ".join(words))
print("-".join(words))
print("".join(["P", "y"]))

# Validation methods
print("Python".isalpha())          # only letters
print("2026".isdigit())            # only digits
print("abc123".isalnum())          # letters or digits
print("   ".isspace())             # only whitespace

# Practical use: check a PIN
pin = "4821"
if pin.isdigit() and len(pin) == 4:
    print("Valid PIN")
else:
    print("PIN must be exactly 4 digits")

# Expected output:
# ['Ana', '21', 'Manila']
# ['Python', 'is', 'fun']
# 3
# ['a', 'b', 'c-d']
# Learn Python today
# Learn-Python-today
# Py
# True
# True
# True
# True
# Valid PIN
