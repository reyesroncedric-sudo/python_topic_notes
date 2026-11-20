# Topic: List Basics
# Difficulty: Easy
# Goal: Get one item (indexing) or several items (slicing) from a list

colors = ["red", "green", "blue", "yellow", "purple"]
#  index:    0       1       2        3         4
#  negative: -5     -4      -3       -2        -1

print(colors[0])       # first item
print(colors[2])       # third item
print(colors[-1])      # last item
print(colors[-2])      # second from the end

# Slicing: list[start:stop]  (the stop index is NOT included)
print(colors[1:4])     # index 1, 2, 3
print(colors[:3])      # from the beginning up to index 2
print(colors[2:])      # from index 2 to the end
print(colors[::2])     # every second item

# Lists are mutable: you can change an item by its index
colors[0] = "orange"
print(colors)

# Expected output:
# red
# blue
# purple
# yellow
# ['green', 'blue', 'yellow']
# ['red', 'green', 'blue']
# ['blue', 'yellow', 'purple']
# ['red', 'blue', 'purple']
# ['orange', 'green', 'blue', 'yellow', 'purple']
