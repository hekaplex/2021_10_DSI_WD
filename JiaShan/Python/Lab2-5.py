'''
Create a program that calculates the estimated hours and minutes for a trip.
Console

Travel Time Calculator
Enter miles: 200
Enter miles per hour: 65
Estimated travel time
Hours: 3
Minutes: 5
Specifications
 The program should only accept integer entries like 200 and 65.
 Assume that the user will enter valid data.
Hint
 Use integers with the integer division and modulus operators to get hours and
minutes.
'''
print('Travel Time Calculator')
miles = int(input('Enter miles: '))
milesperhour = int(input('Enter miles per hour: '))
print('Estimated travel time')
hours = miles//milesperhour
minutes = round(((miles%milesperhour)/milesperhour)*60)
print('Hours: '+str(hours)+'\n'+'Minutes: '+str(minutes))