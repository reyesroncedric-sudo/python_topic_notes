# Topic: String Methods
# Difficulty: Hard
# Goal: Encrypt text with a Caesar cipher and compress repeated characters

# 1) Caesar cipher: shift every letter by k positions in the alphabet
def caesar(message, shift):
    result = ""
    for ch in message:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch                  # keep spaces and punctuation
    return result


secret = caesar("Hello, World!", 3)
print(secret)
print(caesar(secret, -3))                 # a negative shift decodes it
print(caesar("xyz", 3))                   # wraps around the alphabet


# 2) Run-length compression: "aaabbc" -> "a3b2c1"
def compress(text):
    if text == "":
        return ""
    result = ""
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            result += text[i - 1] + str(count)
            count = 1
    result += text[-1] + str(count)
    return result


print(compress("aaabbc"))
print(compress("wwwwbbw"))


# 3) Most frequent character (ignoring spaces)
def most_common_char(text):
    text = text.replace(" ", "").lower()
    best = text[0]
    for ch in text:
        if text.count(ch) > text.count(best):
            best = ch
    return best, text.count(best)


print(most_common_char("Mississippi river"))

# Expected output:
# Khoor, Zruog!
# Hello, World!
# abc
# a3b2c1
# w4b2w1
# ('i', 5)
