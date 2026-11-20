# Topic: String Methods
# Difficulty: Hard
# Goal: Combine several string methods to solve real problems

# 1) Palindrome: reads the same forward and backward (ignore case and symbols)
def is_palindrome(text):
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


print(is_palindrome("Racecar"))
print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("Python"))


# 2) Anagram: same letters in a different order
def is_anagram(a, b):
    a = a.replace(" ", "").lower()
    b = b.replace(" ", "").lower()
    return sorted(a) == sorted(b)


print(is_anagram("Listen", "Silent"))
print(is_anagram("Dormitory", "Dirty room"))
print(is_anagram("Hello", "World"))


# 3) Word frequency counter (ignore punctuation and case)
def word_frequency(sentence):
    counts = {}
    for word in sentence.lower().split():
        word = word.strip(".,!?")
        counts[word] = counts.get(word, 0) + 1
    return counts


print(word_frequency("The cat and the hat. The end!"))


# 4) Title-case every word without title()
def capitalize_words(sentence):
    return " ".join(word[0].upper() + word[1:] for word in sentence.split())


print(capitalize_words("the quick brown fox"))

# Expected output:
# True
# True
# False
# True
# True
# False
# {'the': 3, 'cat': 1, 'and': 1, 'hat': 1, 'end': 1}
# The Quick Brown Fox
