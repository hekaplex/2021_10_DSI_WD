''''
Create a program that calculates the amount of time and fuel for a 1980 Cessna 172N to
fly a specified distance.
Console

Aircraft Fuel Calculator
Distance in nautical miles: 180
Flight time: 1 hour(s) and 30 minute(s)
Required fuel: 16.8 gallons
Continue? (y/n): y
Distance in nautical miles: 121
Flight time: 1 hour(s) and 0 minute(s)
Required fuel: 12.7 gallons
Continue? (y/n): n
Bye!

Specifications
 Assume that a 1980 Cessna 172N can fly 120 nautical miles (knots) per hour.
 Assume that a 1980 Cessna 172N burns 8.4 gallons of gas per hour.
 For safety, add a half hour to the flight time when calculating the amount of required
fuel.
 Round the amount of required fuel to 1 decimal place. For safety, always round up,
never down.
 Assume that the user will enter valid data.
'''
print('Aircraft Fuel Calculator\n')
again = 'y'
while again == 'y':
    print('Aircraft Fuel Calculator')
    dis = int(input('Distance in nautical miles: '))
    a = dis//120
    b = round((dis%120)/2)
    print(f'Flight time: {a} hour(s) and {b} minute(s)')
    fuel = (dis/120+0.5)*8.4
    requiredfuel = round(fuel,1)
    print(f'Required fuel: {requiredfuel} gallons')
    again = input('Continue? (y/n): ')
print('Bye!')