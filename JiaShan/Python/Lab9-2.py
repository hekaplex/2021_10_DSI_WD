'''
Create a program that calculates the monthly payments on a loan and displays formatted
results.

Console
Monthly Payment Calculator
DATA ENTRY
Loan amount: 500000
Yearly interest rate: 5.6
Years: 30
FORMATTED RESULTS
Loan amount: $500,000.00
Yearly interest rate: 5.6%
Number of years: 30
Monthly payment: $2,870.39
Continue? (y/n): y
DATA ENTRY
Loan amount: 500000
Yearly interest rate: 4.3
Years: 30
FORMATTED RESULTS
Loan amount: $500,000.00
Yearly interest rate: 4.3%
Number of years: 30
Monthly payment: $2,474.36
Continue? (y/n): n
Bye!

Specifications
 The interest rate should only have 1 decimal place for both the calculation and the
formatted results.
 The formula for calculating monthly payment is:
monthly_payment = loan_amount * monthly_interest_rate /
(1 - 1 / (1 + monthly_interest_rate) ** months)
 Assume that the user will enter valid data.
'''

import math as m
print('Monthly Payment Calculator')
again = 'y'
while again.lower() == 'y':
    print('DATA ENTRY')
    loan = float(input('Loan amount: '))
    interestrate = float(input('Yearly interest rate: '))
    yearterm = int(input('Years: '))
    i = round(interestrate, 1)/100
    monthi = i/12
    print(loan*i)
    monthpay = loan*monthi/(1 - 1 / (1 + monthi) ** (12*yearterm))
    print('FORMATTED RESULTS')
    print(f'Loan amount: ${loan:,.2f}')
    print(f'Interest rate: {i:.1%}')
    print(f'Number of years: {yearterm}')
    print(f'Monthly payment: ${monthpay:,.2f}')
    again = input('Continue? (y/n): ')
print('Bye!')