# Part A: Saving for a House

#Write a program to calculate how many months it will take you to save up enough money for a down payment. You will want your main variables to be floats, so you should cast user inputs to floats.   
#1. Your program should ask the user to enter the following variables:
#2. The starting annual salary (annual_salary)
#3. The portion of salary to be saved (portion_saved)
#4. The cost of your dream home (total_cost)

# asking user for inputs
yearly_salary = float(input("Please input your starting yearly salary: "))
portion_saved  = float(input("Please input your portion of salary to be saved: "))
cost_of_dream_home = float(input("Please input the cost of your dream home: "))

# setting variables
portion_down_payment = 0.25
amount_saved = 0
monthly_salary = (yearly_salary / 12)
r = 0.05
months = 0

# calculation of down payment before WHILE loop
down_payment = cost_of_dream_home * portion_down_payment

# WHILE loop that ends when savings amount can pay off down payment
while amount_saved < down_payment:
    amount_saved += (monthly_salary * portion_saved) + amount_saved * (r/12)
    months += 1
    #print(amount_saved)

#answer for the user
print("Number of months: ", months)


# Part B: Saving with a raise
#Write a program to calculate how many months it will take you save up enough money for a down payment.  LIke before, assume that your investments earn a return of r = 0.04 (or 4%) and the required down payment percentage is 0.25 (or 25%).  Have the user enter the following variables:
#1. The starting annual salary (annual_salary)
#2. The percentage of salary to be saved (portion_saved)
#3. The cost of your dream home (total_cost)
#4. The semi­annual salary raise (semi_annual_raise)

# asking the user for inputs
yearly_salary = float(input("Please input your starting yearly salary: "))
portion_saved  = float(input("Please input your portion of salary to be saved: "))
cost_of_dream_home = float(input("Please input the cost of your dream home: "))
semi_annual_raise = float(input("Please input your semi annual raise: "))

# setting variables
portion_down_payment = 0.25
amount_saved = 0
r = 0.05
months = 0

# calculation of down payment before WHILE loop
down_payment = cost_of_dream_home * portion_down_payment

# WHILE loop that has an if condition that for every 6 months, a semi annual raise is added onto the yearly salary

while amount_saved < down_payment:
    amount_saved += ((yearly_salary / 12) * portion_saved) + amount_saved * (r/12)
    months += 1
    if months % 6 == 0:
        yearly_salary += (yearly_salary * semi_annual_raise)
        #print(months)
        #print(yearly_salary)

#answer for the user
print("Number of months: ", months)

# Part C: Choosing an Interest Rate
#Write a program to calculate the best savings rate, as a function of your starting salary.
#You should use bisection search to help you do this efficiently. You should keep track of the number of steps it takes your bisections search to finish. You should be able to reuse some of the code you wrote for part B in this problem.  

#variables for "amount saved calculation" while loop
cost = float(800000)
dp = cost * 0.25
r = float(0)
months = 36
amount_saved = 0

#Variables related to r calculation
low = float(0)
high = float(1)
steps = 0

#Input
initial = float(input("Please enter your initial deposit: "))

#flags and tests before "amount saved calculation" while loop starts
flag_already_have_down_payment = 0
flag_impossible = 0
impossible_test = (initial * (1+1/12)**months)

# if initial is already enough to cover down payment(-100) best rate is 0.0
if initial >= (dp-100):
   flag_already_have_down_payment = 1
   r = 0.0
# if rate is already 1.0 (100%) but amount saved is still less than the down payment, this means it's impossible for best rate to be between 0 - 100
elif impossible_test < dp:
    flag_impossible = 1
    r = None

while ((amount_saved < (dp-100)) or (amount_saved > (dp+100))) and flag_already_have_down_payment == 0 and flag_impossible == 0:
    r = (low + high) / 2
    steps += 1
    amount_saved = initial * (1+r/12)**months
    if amount_saved > (dp+100):
        low = low
        high = r
    elif amount_saved < (dp-100):
        low = r
        high = high

print("Best savings rate:", r)
print("Steps in bisection search:", steps)
