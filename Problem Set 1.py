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
down_paynent = cost_of_dream_home * portion_down_payment

# WHILE loop that ends when savings amount can pay off down payment
while amount_saved < down_paynent:
    amount_saved += (monthly_salary * portion_saved) + amount_saved * (r/12)
    months += 1
    #print(amount_saved)

#answer for the user
print("Number of months: ", months)
