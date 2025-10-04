# Assume you are given a variable named number (has a numerical value).
number = int(input('Can you please input a number?: '))

# Write a piece of Python code that prints out one of the following strings: 
    # positive if the variable number is positive
    # negative if the variable number is negative
    # zero if the variable number is equal to zero\\
if number > 0:
    print('positive')
elif number < 0:
    print ('negative')
else:
    print ('zero')