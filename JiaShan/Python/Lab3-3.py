'''
Project 3-3: Change Calculator
Create a program that calculates the coins needed to make change for the specified
number of cents.

Console
Change Calculator
Enter number of cents (0-99): 99
Quarters: 3
Dimes: 2
Nickels: 0
Pennies: 4
Continue? (y/n): y
Enter number of cents (0-99): 55
Quarters: 2
Dimes: 0
Nickels: 1
Pennies: 0
Continue? (y/n): n
Bye!

Specifications
 The program should display the minimum number of quarters, dimes, nickels, and
pennies that one needs to make up the specified number of cents.
 Assume that the user will enter a valid integer for the number of cents.
 The program should continue only if the user enters “y” or “Y” to continue.
'''
print('Change Calculator')
money = int(input('Enter number of cents (0-99):'))
flag = 'y'
while flag.lower() == 'y':
    q = money//25
    d = (money-25*q)//10
    n = (money-25*q-10*d)//5
    p = money-25*q-10*d-5*n
    print(f'Quaters: {q}')
    print(f'Dimes: {d}')
    print(f'Nickels: {n}')
    print(f'Pennies: {p}')
    flag = input('Continue? (y/n): ')
print('Bye!')

