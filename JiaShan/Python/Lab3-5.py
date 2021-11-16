'''
Project 3-5: Table of Powers
Create a program that displays a table of squares and cubes for the specified range of
numbers.

Console
Table of Powers
Start number: 90
Stop number: 100
Number Squared Cubed
====== ======= =====
90 8100 729000
91 8281 753571
92 8464 778688
93 8649 804357
94 8836 830584
95 9025 857375
96 9216 884736
97 9409 912673
98 9604 941192
99 9801 970299
100 10000 1000000

Specifications
 The formulas for calculating squares and cubes are:
square = x ** 2
cube = x ** 3
 Use tabs to align the columns.
 Assume that the user will enter valid integers.
 Make sure the user enters a start integer that’s less than the stop integer. If the user
enters a start integer that’s greater than the stop integer, display an error message and
give the user a chance to enter the integers again.
'''
# display program title
print("Table of Powers")
print()

# get input from the user
while True:
    start = int(input("Start number: "))
    stop  = int(input("Stop number:  "))
    if start > stop:
        print("Start number must be less than stop number. Please try again.\n")
        continue
    else:
        print()
        break

print("Number\tSquared\tCubed")
print("======\t=======\t=====")
for number in range(start, stop+1):
    print(f"{number}\t{number**2}\t{number**3}")