# Assume you are given a positive integer variable named N.
# Write a piece of Python code that prints hello world on separate lines, N times.
# You can use either a while loop or a for loop.

N = int(input("Please input a positive integer variable: "))

# while loop
while N > 0:
    print ("Hello World")
    N -= 1

# for loop just so I learn
for line in range(N):
    print ("Hello World")