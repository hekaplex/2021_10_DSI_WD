'''Project 4-3: Feet and Meters Converter
Create a program that uses a separate module to convert feet to meters and vice versa.
Console

Feet and Meters Converter

Conversions Menu:
a. Feet to Meters
b. Meters to Feet
Select a conversion (a/b): a
Enter feet: 100
30.48 meters
Would you like to perform another conversion? (y/n): y
Conversions Menu:
a. Feet to Meters
b. Meters to Feet
Select a conversion (a/b): b
Enter meters: 100
328.08 feet
Would you like to perform another conversion? (y/n): n
Thanks, bye!
Specifications
 The formula for converting feet to meters is:
feet = meters / 0.3048
 The formula for converting meters to feet is:
meters = feet * 0.3048
 Store the code that performs the feet to meters and meters to feet conversions in
functions within a module.
 Store the code that displays the title in its own function, and store the code that
displays the menu in its own function, but store the rest of the code that gets input
and displays output in the main() function.
 Assume the user will enter valid data.
 The program should round results to a maximum of two decimal places.'''

def title():
    print("\nFeet and Meters Converter")


def menu():
    print("\nConversions Menu:\na. Feet to Meters\nb. Meters to Feet\n")


def feetToMeters(distanceNumber):
    feet = float(distanceNumber*.3048)
    return feet
def metersToFeet(distanceNumber):
    meters = float(distanceNumber/.3048)
    return meters
    
def main():
    
    title()
    
    tryAgainChoice = "y"
    while tryAgainChoice == "y":
        
        menu()

        convertChoice = input("Select a conversion (a/b): ")
        
        if convertChoice.lower() == "a":
            distanceNumber = float(input("Enter number of feet to convert: "))
            print(str(round(feetToMeters(distanceNumber),2)) + " meters")
        elif convertChoice == "b":
            distanceNumber = float(input("Enter number of meters to convert: "))
            print(str(round(metersToFeet(distanceNumber),2)) + " feet")
        else:
            print("Invalid entry. Please enter 'a' or 'b'")

        tryAgainChoice = input("Would you like to perform another conversion? (y/n): ")

    print("Bye")

if __name__ == "__main__":
    main()