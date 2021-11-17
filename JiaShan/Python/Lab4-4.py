'''
Create a program that uses a separate module to calculate sales tax and total after tax.
Console

Sales Tax Calculator
ENTER ITEMS (ENTER 0 TO END)
Cost of item: 35.99
Cost of item: 27.50
Cost of item: 19.59
Cost of item: 0
Total: 83.08
Sales tax: 4.98
Total after tax: 88.06
Again? (y/n): y
ENTER ITEMS (ENTER 0 TO END)
Cost of item: 152.50
Cost of item: 59.80
Cost of item: 0
Total: 212.3
Sales tax: 12.74
Total after tax: 225.04
Again? (y/n): n
Thanks, bye!

Specifications
 The sales tax rate should be 6% of the total.
 Store the sales tax rate in a module. This module should also contain functions that
calculate the sales tax and the total after tax. These functions should round the results
to a maximum of two decimal places.
 Store the code that gets input and displays output in the main() function. Divide this
code into functions whenever you think it would make that code easier to read and
maintain.
 Assume the user will enter valid data.
'''

import salestax as st
def itemtotal():
    print('ENTER ITEMS (ENTER 0 TO END)')
    total = 0
    while True:
        costofitem = float(input('Cost of item: '))
        if costofitem == 0:
            break
        total += costofitem
    return round(total, 2)
def main():
    print('Sales Tax Calculator')
    choice = 'y'
    while choice == 'y':
        total = itemtotal()
        print(f'Total: {total}')
        print(f'Sales tax: {st.salestax(total)}')
        print(f'Total after tax: {st.aftertaxtotoal(total)}')
        choice = input(('Again? (y/n): '))
    print('Thanks, bye!')
if __name__ == "__main__":
    main()