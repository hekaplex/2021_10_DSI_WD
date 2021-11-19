'''Project 3-4: Shipping Calculator
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
the user a chance to enter the number again.'''

print("=========================================================\nShipping Calculator\n=========================================================")

continueChoice = "y"

while continueChoice == "y":

    costOfOrder = float(input("Cost of items ordered:\t"))
    shippingCost = 0
    
    if costOfOrder < 0:
        print("Entry not acceptable.  Please enter a valid entry.")
        continue
        
    elif costOfOrder < 30.00:
        shippingCost = 5.95
        print("Shipping Cost:\t\t5.95")
        print("Total cost:\t\t" + str(round(costOfOrder+shippingCost,2)))

    elif costOfOrder >= 30.00 and costOfOrder < 50.00:
        shippingCost = 7.95
        print("Shipping cost:\t\t7.95")
        print("Total cost:\t\t" + str(round(costOfOrder+shippingCost,2)))
    
    elif costOfOrder >= 50.00 and costOfOrder < 75.00:
        shippingCost = 9.95
        print("Shipping cost:\t\t9.95")
        print("Total cost:\t\t" + str(round(costOfOrder+shippingCost,2)))
    
    else:
        shippingCost = 0
        print("Shipping cost:\t\tfree")
        print("Total cost\t\t" + str(round(costOfOrder+shippingCost,2)))
        
    continueChoice = input("Would you like to calculate another order (y/n)?")

print("Goodbye")
    
    
