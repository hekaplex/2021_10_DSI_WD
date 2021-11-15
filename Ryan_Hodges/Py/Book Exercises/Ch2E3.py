'''
Project 2-3: Tip Calculator
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

costOfMeal = float(input("Cost of meal: "))
tipPercent = float(input("Tip percent: "))
tipAmount = round(costOfMeal*(tipPercent/100),2)

print("\nTip Amount: \t" + str(tipAmount))
print("Total Amount: \t" + str(round(costOfMeal+tipAmount,2)))