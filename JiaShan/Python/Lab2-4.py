'''
Create a program that compares the unit prices for two sizes of laundry detergent sold at a
grocery store.
Console

Price Comparison
Price of 64 oz size: 5.99
Price of 32 oz size: 3.50
Price per oz (64 oz): 0.09
Price per oz (32 oz): 0.11

Specifications
 The formula for calculating price per ounce is:
price per ounce = price / ounces
 Assume the user will enter valid data.
 The program should round the results to a maximum of two decimal places.
'''
print('Price Comparison')
price64 = float(input('Enter the price for 64 oz size: '))
price32 = float(input('Enter the price for 32 oz size: '))
unitprice64 = round(price64/64, 2)
unitpirce32 = round(price32/32, 2)
print('Price of 64 oz size: '+str(price64)+'\n'+'Price of 32 oz size: '+str(price32)+'\n'+'Price per oz (64 oz): '+str(unitprice64)+'\n'+'Price per oz (32 oz): '+str(unitpirce32))