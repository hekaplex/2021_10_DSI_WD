'''Project 3-3: Change Calculator
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
 The program should continue only if the user enters “y” or “Y” to continue.'''

print("Change Calculator")

continueChoice = "y"
quarter = 25
dime = 10
nickel = 5
penny = 1


while continueChoice == "y":

    numberOfCents = int(input("Enter number of cents (0-99): "))
    quarterTotal = int(numberOfCents//quarter)
    dimeTotal = int((numberOfCents-(quarterTotal*quarter))//dime)
    nickelTotal = int((numberOfCents-(quarterTotal*quarter)-(dimeTotal*dime))//nickel)
    pennyTotal = int(numberOfCents-(quarterTotal*quarter)-(dimeTotal*dime)-(nickelTotal*nickel))

    print("Quarters:\t" + str(quarterTotal))
    print("Dimes:\t\t" + str(dimeTotal))
    print("Nickels:\t" + str(nickelTotal))
    print("Pennies:\t" + str(pennyTotal))

    continueChoice = input("Would you like to enter another number (y/n)? ")

print("Have a great day")