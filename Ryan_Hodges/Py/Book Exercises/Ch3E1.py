'''
Project 3-1: Letter Grade Converter
Create a program that converts number grades to letter grades.
Console
Letter Grade Converter
Enter numerical grade: 90
Letter grade: A
Continue? (y/n): y
Enter numerical grade: 88
Letter grade: A
Continue? (y/n): y
Enter numerical grade: 80
Letter grade: B
Continue? (y/n): y
Enter numerical grade: 67
Letter grade: C
Continue? (y/n): y
Enter numerical grade: 59
Letter grade: F
Continue? (y/n): n
Bye!
Specifications
 The grading criteria is as follows:
A 88-100
B 80-87
C 67-79
D 60-66
F <60
 Assume that the user will enter valid integers for the grades.
 The program should continue only if the user enters “y” or “Y” to continue.
'''


continueChoice = "y"

while continueChoice.lower() == "y":

    numberGrade = int(input("Enter grade: "))

    if numberGrade > 100:
        print("Grade must be 100 or less.  Reenter the grade.")
    elif numberGrade >= 88 and numberGrade <= 100:
        print("A")
    elif numberGrade >= 80 and numberGrade < 88:
        print("B")
    elif numberGrade >= 67 and numberGrade < 80:
        print("C")
    elif numberGrade >= 60 and numberGrade < 67:
        print("D")
    else:
        print("F")

    continueChoice = input("Would you like to enter another grade? ")

print("Farewell")