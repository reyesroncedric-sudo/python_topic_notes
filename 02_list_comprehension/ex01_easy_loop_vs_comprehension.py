# Topic: List Comprehension
# Difficulty: Easy
# Goal: Build the same list with a for loop and with a list comprehension

# Syntax:  new_list = [expression for item in iterable]

# Traditional for loop (3 lines)
numbers = []
for i in range(1, 6):
    numbers.append(i)
print(numbers)

# List comprehension (1 line)
numbers = [i for i in range(1, 6)]
print(numbers)

# Another comparison: multiply every number by 10
loop_result = []
for i in range(1, 6):
    loop_result.append(i * 10)

comp_result = [i * 10 for i in range(1, 6)]

print(loop_result)
print(comp_result)
print(loop_result == comp_result)    # both give the same list

# Expected output:
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]
# [10, 20, 30, 40, 50]
# [10, 20, 30, 40, 50]
# True
