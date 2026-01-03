# Assume you are given an integer greater than 0 and less than or equal to 1000
# Write a piece of Python code that uses bisection search to guess N.
# The code prints two lines: count: with how many guesses it took to find N, and answer: with the value of N.
# Hints: If the halfway value is exactly in between two integers, choose the smaller one.

low = 0
high = 1001
n = 15
x = 0
guesses = 0

while x != n:
    x = (low + high)/2
    guesses += 1
    if x > n:
        high = x
    elif x < n:
        low = x
    else:
        print (x)
        break

print(guesses)