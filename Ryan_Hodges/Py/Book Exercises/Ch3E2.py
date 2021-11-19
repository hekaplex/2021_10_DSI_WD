'''Project 3-2: Tip Calculator
Create a program that calculates three options for an appropriate tip to leave after a meal
at a restaurant.
Console
Tip Calculator
Cost of meal: 52.31
15%
Tip amount: 7.85
Total amount: 60.16
20%
Tip amount: 10.46
Total amount: 62.77
25%
Tip amount: 13.08
Total amount: 65.39
Specifications
 The program should calculate and display the cost of tipping at 15%, 20%, or 25%.
 Assume the user will enter valid data.
 The program should round results to a maximum of two decimal places.'''

print("\nTip Calculator")

costOfMeal = float(input("Cost of meal: "))

print("\n15%\nTip amount:\t" + str(round(costOfMeal*.15,2)))
print("Total amount:\t" + str(round(costOfMeal+round(costOfMeal*.15,2),2)))

print("\n20%\nTip amount:\t" + str(round(costOfMeal*.2,2)))
print("Total amount:\t" + str(round(costOfMeal+round(costOfMeal*.2,2),2)))

print("\n25%\nTip amount:\t" + str(round(costOfMeal*.25,2)))
print("Total amount:\t" + str(round(costOfMeal+round(costOfMeal*.25,2),2)))