# Assume you are given a positive integer variable named N. Write a piece of Python code that finds the cube root of N.
# The code prints the cube root if N is a perfect cube or it prints error if N is not a perfect cube.
# Hint: use a loop that increments a counter—you decide when the counter should stop.

N = 25
guess = 0

while guess ** 2 < N:
    guess += 1

if guess ** 2 == N:
    print("This is a perfect square! The cube root of",N,"is",guess,"!"  )
elif guess **2 > N:
    print("This is not a perfect square unfortunately.")