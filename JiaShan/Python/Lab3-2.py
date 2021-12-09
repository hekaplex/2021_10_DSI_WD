'''
Project 3-2: Tip Calculator
Create a program that calculates three options for an appropriate tip to leave after a meal
at a restaurant.

Console
Tip Calculator
Cost of meal: 52.31
15%
Tip amount: 7.85
Total amount: 60.16
20%
Tip amount: 10.46
Total amount: 62.77
25%
Tip amount: 13.08
Total amount: 65.39

Specifications
 The program should calculate and display the cost of tipping at 15%, 20%, or 25%.
 Assume the user will enter valid data.
 The program should round results to a maximum of two decimal places.
'''
print('Tip Calculator')
costofmeal = float(input('Cost of meal: '))
print()
tippercent = 15
while tippercent <= 29:
    totalamount = round((costofmeal+costofmeal*tippercent/100), 2)
    print(f'{tippercent}%')
    print(f'Total amount: {totalamount}')
    print()
    tippercent += 5
print('Thank you! Please choose from one of above options or customize your own.')