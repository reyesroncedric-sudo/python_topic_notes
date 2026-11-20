# Topic: List Comprehension
# Difficulty: Hard
# Goal: Solve harder problems and learn when a comprehension is too much

# 1) Prime numbers up to 30
#    A number is prime if no number from 2 up to its square root divides it.
primes = [n for n in range(2, 31)
          if all(n % d != 0 for d in range(2, int(n ** 0.5) + 1))]
print(primes)

# 2) Pythagorean triples (a, b, c) where a*a + b*b == c*c and c <= 20
triples = [(a, b, c)
           for a in range(1, 21)
           for b in range(a, 21)
           for c in range(b, 21)
           if a * a + b * b == c * c]
print(triples)

# 3) FizzBuzz for 1 to 15
fizzbuzz = ["FizzBuzz" if n % 15 == 0
            else "Fizz" if n % 3 == 0
            else "Buzz" if n % 5 == 0
            else n
            for n in range(1, 16)]
print(fizzbuzz)

# 4) Words longer than the average word length
words = ["a", "python", "is", "great", "language"]
average = sum(len(w) for w in words) / len(words)
longer = [w for w in words if len(w) > average]
print(average)
print(longer)

# WHEN NOT TO USE A COMPREHENSION
# If the logic needs many steps, a normal for loop is easier to read and maintain.
# The FizzBuzz above is already close to the limit of readable.

# Expected output:
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# [(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (9, 12, 15), (12, 16, 20)]
# [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
# 4.4
# ['python', 'great', 'language']
