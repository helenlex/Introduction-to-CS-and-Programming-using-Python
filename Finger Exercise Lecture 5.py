# Assume you are given a string variable named my_str.
# Write a piece of Python code that prints out a new string containing the even indexed characters of my_str.
# For example, if my_str = "abcdefg" then your code should print out aceg.

my_str = 'abcdefg'
even_characters = ''

for x in range(len(my_str)):
    if x % 2 == 0:
        even_characters += (my_str[x])


print (even_characters)