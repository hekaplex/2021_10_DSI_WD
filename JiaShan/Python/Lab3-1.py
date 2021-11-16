'''
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
print('Letter Grade Coverter')
flag = 'y'
while flag.lower() == 'y':
    grade = int(input('Enter numerical grade: '))
    if grade >= 88 and grade <= 100:
        print('Letter grade: A')
    elif grade >= 80 and grade <= 87:
        print('Letter grade: B')
    elif grade >= 67 and grade <= 79:
        print('Letter grade: C')
    elif grade >= 60 and grade <= 66:
        print('Letter grade: D')
    else:
        print('Letter grade: F')
    flag = input('Do you want to continue? Y/N\t')
print('Bye!')