'''
Create a program that keeps track of the items that a wizard can carry.
Console

The Wizard Inventory program
COMMAND MENU
show - Show all items
grab - Grab an item
edit - Edit an item
drop - Drop an item
exit - Exit program
Command: show
1. wooden staff
2. wizard hat
3. cloth shoes
Command: grab
Name: potion of invisibility
potion of invisibility was added.
Command: grab
You can't carry any more items. Drop something first.
Command: show
1. wooden staff
2. wizard hat
3. cloth shoes
4. potion of invisibility
Command: edit
Number: 1
Updated name: magic wooden staff
Item number 1 was updated.
Command: drop
Number: 3
cloth shoes was dropped.
Command: exit
Bye!
Specifications

 Use a list to store the items. Provide three starting items.
 The wizard can only carry four items at a time.
 For the edit and drop commands, display an error message if the user enters an
invalid number for the item.
 When you exit the program, all changes that you made to the inventory are lost.
'''
def display():
    print('The Wizard Inventory program\nCOMMAND MENU\nshow - Show all items\ngrab - Grab an item\nedit - Edit an item\ndrop - Drop an item\nexit - Exit program')
    
def inventorylist(inventory):
    for i, item in enumerate(inventory, start=1):
        print(f'{i}. {item}')

def add(inventory):
    while True:
        whatwehave = input('Name: ')
        inventory.append(whatwehave)
        if len(inventory) < 5:
            print(f'{whatwehave} was added.')
            break
        else:
            print(f"You can't carry any more items. Drop something first.")
            return

def edit(inventory):
    pick = int(input('Number: '))
    if pick < 1 or pick > len(inventory):
        print("Invalid number, please check inventory number")
    else:
        update = input('Updated name:')
        inventory[pick-1] = update
        print(f"Item number {pick} was updated.")

def delete(inventory):
    pick = int(input('Number: '))
    if pick < 1 or pick > len(inventory):
        print("Invalid number, please check inventory number")
    else:        
        whatwelost = inventory.pop(pick-1)
        print(f"{whatwelost} was dropped.")

def main():
    wizardinventory = ['wooden staff',
                       'wizard hat',
                       'cloth shoes']
    display()
    while True:
        command = input('Command: ')
        if command == 'show':
            inventorylist(wizardinventory)
        elif command == 'grab':
            add(wizardinventory)
        elif command == 'edit':
            edit(wizardinventory)
        elif command == 'drop':
            delete(wizardinventory)
        elif command == 'exit':
            break
        else:
            print('Please choose one of the following commands:\nshow - Show all items\ngrab - Grab an item\nedit - Edit an item\ndrop - Drop an item\nexit - Exit program')
    print("Bye!")
if __name__ == "__main__":
    main()