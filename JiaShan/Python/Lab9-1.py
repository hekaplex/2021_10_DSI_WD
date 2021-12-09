'''
Create a program that calculates the interest on a loan and displays formatted results.
Console

Interest Calculator
Enter loan amount: 520000
Enter interest rate: 5.375
Loan amount: $520,000.00
Interest rate: 5.375%
Interest amount: $27,950.00
Continue? (y/n): y
Enter loan amount: 4944.5
Enter interest rate: 1.3
Loan amount: $4,944.50
Interest rate: 1.300%
Interest amount: $64.28
Continue? (y/n): n
Bye!

Specifications

 The formula for calculating the interest amount is:
loan_amount * (interest_rate / 100)
 Use the Decimal class to make sure that all calculations are accurate. It should round
the interest that’s calculated to two decimal places, rounding up if the third decimal
place is five or greater.
 The interest rate that’s displayed can have up to 3 decimal places.
 Assume that the user will enter valid decimal values for the loan amount and interest
rate.
'''
import math as m
print('Interest Calculator')
again = 'y'
while again.lower() == 'y':
    loan = float(input('Enter loan amount: $'))
    interestrate = float(input('Enter interest rate:'))
    i = round(interestrate, 2)/100
    interestamount = loan*i
    print(f'Loan amount: ${loan:,.2f}')
    print(f'Interest rate: {i:.3%}')
    print(f'Interest amount: ${interestamount:,.2f}')
    again = input('Continue? (y/n): ')
print('Bye!')
