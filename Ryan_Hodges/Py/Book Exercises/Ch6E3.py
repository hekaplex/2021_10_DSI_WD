'''Project 6-3: Contact Manager 
Create a program that a user can use to manage the primary email address and phone 
number for a contact. 
Console 
Contact Manager 
COMMAND MENU 
list - Display all contacts 
view - View a contact 
add - Add a contact 
del - Delete a contact 
exit - Exit program 
Command: list
1. Guido van Rossum 
2. Eric Idle 
Command: view 
Number: 2
Name: Eric Idle 
Email: eric@ericidle.com 
Phone: +44 20 7946 0958 
Command: add 
Name: Mike Murach 
Email: mike@murach.com 
Phone: 559-123-4567
Mike Murach was added. 
Command: del
Number: 1
Guido van Rossum was deleted. 
Command: list
1. Eric Idle 
2. Mike Murach 
Command: exit 
Bye! 
Specifications 
 Use a list of lists to store the data for the contacts. Provide starting data for two or 
more contacts. 
 For the view and del commands, display an error message if the user enters an invalid 
contact number. 
 When you exit the program, all changes that you made to the contact list are lost.
'''

def welcome():
    print("\nContact Manager")

def commandMenu():
    print("\nCOMMAND MENU")
    print("list - Display all contacts")
    print("view - View a contact")
    print("add - Add a contact")
    print("delete - Delete a contact")
    print("exit - Exit program")
    commandSelection = input("\nEnter desired action:\n\t")
    return commandSelection

def list(contacts):
    print()
    for i, row in enumerate(contacts, start=1):
        print(f"{i}. {row[0]}")
        

def view(contact):
    for i, row in enumerate(contact, start=1):
        print(f"{i}. {row[0]}")
    viewContact = input("Enter number of contact to view:\n\t")
    print(contact[int(viewContact)-1])

def add(contacts):
    newName = input("Enter name: ")
    newEmail = input("Enter email address: ")
    newPhone = input("Enter phone number:\n+## ## #### #### ")
    contact = [newName,newEmail,newPhone]
    contacts.append(contact)
    print(newName + " was added")

def delete(contact):
    for i, row in enumerate(contact, start=1):
        print(f"{i}. {row[0]}")
    deleteContact = input("Select number of contact to delete:\n")
    print(str(contact[int(deleteContact)-1]) + " was deleted.")
    contact.pop(int(deleteContact)-1)
    

def main():
    welcome()

    contactsList = [["Eric Idle", "eric@ericidle.com","+44 20 7946 0958"],
                    ["Mike Murach","mike@mikemurach.com","+44 20 1234 5678"]]

    while True:
        commandSelection = commandMenu()
        if commandSelection.lower() == "list":
            list(contactsList)
        elif commandSelection.lower() == "view":
            view(contactsList)
        elif commandSelection.lower() == "add":
            add(contactsList)
        elif commandSelection.lower() == "delete":
            delete(contactsList)
        elif commandSelection.lower() == "exit":
            break

    print("bye")

if __name__ == "__main__":
    main()