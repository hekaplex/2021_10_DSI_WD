'''
completion message that includes the user’s full name and a temporary password.

Console
Registration Form
First name: Eric
Last name: Idle
Birth year: 1934
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
print('Console''\n''Registration Form')
firstname = input('Enter your first name: ')
lastname = input('Enter you last name: ')
birthyear = input('Enter your 4 digit birth year: ')
print('Welcome '+firstname+' '+lastname+'!''\n''Your registration is complete.''\n''Your temperary password is: '+firstname+'*'+birthyear)

