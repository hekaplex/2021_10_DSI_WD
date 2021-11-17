'''
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
 The program should round results to a maximum of two decimal places.
'''

def feettometer(feet):
    meter = feet*0.3048
    return round(meter, 2)
def metertofeet(meter):
    feet = meter/0.3048
    return round(feet, 2)
def main():
    print('Feet and Meters Converter\nConversions Menu:\na. Feet to Meters\nb. Meters to Feet')
    choice = 'y'
    while choice == 'y':
        flag = input(('Select a conversion (a/b): '))
        if flag.lower() == 'a':
            feet = float(input('Enter feet: '))
            print(f'{feettometer(feet)} meters')
        else:
            meter = float(input('Enter meters: '))
            print(f'{metertofeet(meter)} feet')
        choice = input(('Would you like to perform another conversion? (y/n): '))
    print('Thanks, bye!')
if __name__ == "__main__":
    main()