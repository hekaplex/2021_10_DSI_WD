'''
Project 3-4: Shipping Calculator
Create a program that calculates the total cost of an order including shipping.
Console

===============================================================
Shipping Calculator
===============================================================
Cost of items ordered: 49.99
Shipping cost: 7.95
Total cost: 57.94
Continue? (y/n): y
===============================================================
Cost of items ordered: -65.50
You must enter a positive number. Please try again.
Cost of items ordered: 65.50
Shipping cost: 9.95
Total cost: 75.45
Continue? (y/n): n
===============================================================
Bye!

Specifications
 Use the following table to calculate shipping cost:
COST OF ITEMS SHIPPING COST
==============================
< 30.00 5.95
30.00-49.99 7.95
50.00-74.99 9.95
>= 75.00 FREE
 If the user enters a number that’s less than zero, display an error message and give
the user a chance to enter the number again.
'''
print('===============================================================')
print('Shipping Calculator')
print('===============================================================')
flag = 'y'
while flag.lower() == 'y':
    cost = round(float(input('Cost of items ordered: ')), 2)
    shipping = 5.95
    if cost > 0 and cost < 30.00:
        total = cost + shipping
        print('Shipping Cost: ',shipping)
        print('Total cost: ', total)
    elif cost >= 30.00 and cost < 49.99:
        shipping += 2
        total = cost + shipping
        print('Shipping Cost: ',shipping)
        print('Total cost: ', total)
    elif cost >= 50.00 and cost < 74.99:
        shipping += 4
        total = cost + shipping
        print('Shipping Cost: ',shipping)
        print('Total cost: ', total)
    elif cost >= 75.00:
        shipping = 0
        total = cost
        print('Shipping Cost: ',shipping)
        print('Total cost: ', total)
    else:
        print('You must enter a positive number. Please try again.')
    flag = input('Continue? (y/n): ')
print('===============================================================')
print('Bye!')