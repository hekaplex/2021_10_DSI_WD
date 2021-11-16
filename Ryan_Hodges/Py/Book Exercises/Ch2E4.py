'''
Project 2-4: Price Comparison
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

priceOf64OZ = float(input("Price for 64 oz: "))
priceOf32OZ = float(input("Price for 32 oz: "))
pricePerOZbig = float(priceOf64OZ/64)
pricePerOZsmall = float(priceOf32OZ/32)

print("\nPrice per oz (64 oz): " + str(round(pricePerOZbig,2)))
print("Price per oz (32 oz): " + str(round(pricePerOZsmall,2)))