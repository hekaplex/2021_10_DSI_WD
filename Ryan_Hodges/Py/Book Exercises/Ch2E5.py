'''
Project 2-5: Travel Time Calculator
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

milesToLocation = int(input("Miles to Destination: "))
milesPerHour = int(input("Travel speed: "))
hoursToDestination = milesToLocation//milesPerHour
minutesToDestination = milesToLocation%milesPerHour

print("\n Hours: \t" + str(hoursToDestination))
print("Minutes: \t" + str(minutesToDestination))