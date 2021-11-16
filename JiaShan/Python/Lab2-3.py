'''
Create a program that calculates the tip and total for a meal at a restaurant.
Console

Tip Calculator
Cost of meal: 52.31
Tip percent: 20
Tip amount: 10.46
Total amount: 62.77

Specifications
 The formula for calculating the tip amount is:
tip = cost of meal * (tip percent / 100)
 The program should accept decimal entries like 52.31 and 15.5.
 Assume the user will enter valid data.
 The program should round the results to a maximum of two decimal places.
'''
print('Tip Calculator')
cost_of_meal = float(input('Enter your meal cost here: '))
tip_percent = float(input('Enter your tip percent here: '))
tip_amount = round(float(cost_of_meal*(tip_percent/100)), 2)
total_amount = round(float(cost_of_meal+tip_amount), 2)
print('Tip persent: '+str(tip_percent))
print('Tip amount: '+str(tip_amount))
print('Total amount: '+str(total_amount))