'''
Project 2-1: Student Registration
Create a program that allows a student to complete a registration form and displays a
completion message that includes the user’s full name and a temporary password.
Console

Registration Form
First name:     Eric
Last name:      Idle
Birth year:     1934

Welcome Eric Idle!
Your registration is complete.
Your temporary password is: Eric*1934


Specifications
 The user’s full name consists of the user’s first name, a space, and the user’s last
name.
 The temporary password consists of the user’s first name, an asterisk (*), and the
user’s birth year.
 Assume the user will enter valid data.
'''

firstName = input("What is your first name? ")

lastName = input("What is your last name? ")

birthYear = input("What year were you born? ")

print("\n\nWelcome " + firstName + " " + lastName,end='!'"\n")
print("Your registration is complete.\nYour temporary password is: " + firstName + str("*") + str(birthYear))