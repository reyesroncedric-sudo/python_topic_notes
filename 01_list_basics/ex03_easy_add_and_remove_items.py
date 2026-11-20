# Topic: List Basics
# Difficulty: Easy
# Goal: Add and remove items using list methods

pets = ["dog", "cat"]

# --- Adding items ---
pets.append("fish")            # add to the END
print(pets)

pets.insert(1, "bird")         # insert at index 1
print(pets)

pets.extend(["hamster", "rabbit"])   # add many items at once
print(pets)

# --- Removing items ---
pets.remove("cat")             # remove by VALUE (first match)
print(pets)

last = pets.pop()              # remove the LAST item and give it back
print("Popped:", last)

first = pets.pop(0)            # remove the item at index 0
print("Popped:", first)

del pets[0]                    # delete by index (no value returned)
print(pets)

pets.clear()                   # remove everything
print(pets)

# Expected output:
# ['dog', 'cat', 'fish']
# ['dog', 'bird', 'cat', 'fish']
# ['dog', 'bird', 'cat', 'fish', 'hamster', 'rabbit']
# ['dog', 'bird', 'fish', 'hamster', 'rabbit']
# Popped: rabbit
# Popped: dog
# ['fish', 'hamster']
# []
