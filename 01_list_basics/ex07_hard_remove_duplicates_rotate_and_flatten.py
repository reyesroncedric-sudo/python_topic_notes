# Topic: List Basics
# Difficulty: Hard
# Goal: Solve classic list problems with functions

# 1) Remove duplicates but KEEP the original order
def remove_duplicates(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result


print(remove_duplicates([3, 1, 3, 2, 1, 4]))


# 2) Rotate a list to the right by k positions
def rotate_right(items, k):
    k = k % len(items)               # handles k bigger than the list length
    if k == 0:
        return items[:]
    return items[-k:] + items[:-k]   # last k items go to the front


print(rotate_right([1, 2, 3, 4, 5], 2))
print(rotate_right([1, 2, 3, 4, 5], 7))   # 7 behaves like 2


# 3) Flatten a list of lists into one list
def flatten(nested):
    flat = []
    for sub in nested:
        flat.extend(sub)
    return flat


print(flatten([[1, 2], [3, 4], [5]]))


# 4) Second largest value (without sort tricks that break on duplicates)
def second_largest(numbers):
    unique = remove_duplicates(numbers)
    unique.sort()
    return unique[-2]


print(second_largest([10, 40, 40, 30, 20]))

# Expected output:
# [3, 1, 2, 4]
# [4, 5, 1, 2, 3]
# [4, 5, 1, 2, 3]
# [1, 2, 3, 4, 5]
# 30
