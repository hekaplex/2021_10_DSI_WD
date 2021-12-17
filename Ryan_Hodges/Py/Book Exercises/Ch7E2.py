'''Project 7-2: Wizard Inventory 
Create a program that keeps track of the items that a wizard is carrying. 
Console 
The Wizard Inventory program 
COMMAND MENU 
walk - Walk down the path 
show - Show all items 
drop - Drop an item 
exit - Exit program 
Command: walk
While walking down a path, you see a scroll of uncursing. 
Do you want to grab it? (y/n): y
You picked up a scroll of uncursing. 
Command: walk
While walking down a path, you see an unknown potion. 
Do you want to grab it? (y/n): y 
You can't carry any more items. Drop something first. 
Command: show 
1. a wooden staff 
2. a scroll of invisibility 
3. a crossbow 
4. a scroll of uncursing 
Command: drop
Number: 3
You dropped a crossbow. 
Command: exit 
Bye! 
Specifications 
 Your instructor should provide a text file named wizard_all_items.txt that contains a 
list of all the items that a wizard can carry. 
 You should create another text file named wizard_inventory.txt to store the current 
items that the wizard is carrying. 
 A wizard can only carry four items at a time, and those four items must be different. 
 When the user selects the walk command, the program should read the items from the 
file, create a list of the items that aren’t already in the wizard’s inventory, randomly 
pick one of those items, and give the user the option to grab it. To create a list of the 
items that aren’t already in the wizard’s inventory, you can use a list comprehension 
as described in chapter 6. 
 Make sure to update the inventory text file you created every time the user grabs or 
drops an item. 
 For the drop command, display an error message if the user enters an invalid number 
for the item.
'''

import random

AVAILABLE_ITEMS = "C:\\Users\\Hoegi\\Documents\\Divergence Work\\Python\\Exercise Files\\wizard_all_items.txt"
CURRENT_INVENTORY = "C:\\Users\\Hoegi\\Documents\\Divergence Work\\Python\\Exercise Files\\wizard_inventory.txt"

def welcome():
    print("\nThe Wizard Inventory Program")

def readItems():
    items = []
    with open("C:\\Users\\Hoegi\\Documents\\Divergence Work\\Python\\Exercise Files\\wizard_all_items.txt","r") as file:
        for line in file:
            line = line.replace("\n","")
            items.append(line)
    return items

def readInventory():
    inventory = []
    with open("C:\\Users\\Hoegi\\Documents\\Divergence Work\\Python\\Exercise Files\\wizard_all_items.txt","r") as file:
        for line in file:
            line = line.replace("\n","")
            inventory.append(line)
    return inventory

def writeInventory():
    inventory = []
    with open("C:\\Users\\Hoegi\\Documents\\Divergence Work\\Python\\Exercise Files\\wizard_all_items.txt","w") as file:
        for item in file:
            file.write(item + "\n")

def commandMenu():
    print("\nCOMMAND MENU")
    print("\nshow - Shows all items")
    print("walk - Grabs an item")
    print("drop - Drops an item")
    print("exit - Exits program")
    commandSelection = input("\nType name of action to take.\n")
    return commandSelection

def show(inventory):
    for i, item in enumerate(inventory, start=1):
        print(f"{i}. {item}")
    print()

def walk(inventory):
    
    
    itemsNotInInventoryList = []
    randomItem = random.choice(itemsNotInInventoryList)
    itemPickUpChoice = input(f"You come across a {randomItem}, would you like to pick it up? (y/n) ")
    


    if len(inventory) <= 4:
        inventory.append(randomItem)
    else:
        print("Inventory is full.  You must drop an item in order to gain a new one.")

''' When the user selects the walk command, the program should read the items from the 
file, create a list of the items that aren’t already in the wizard’s inventory, randomly 
pick one of those items, and give the user the option to grab it. To create a list of the 
items that aren’t already in the wizard’s inventory, you can use a list comprehension 
as described in chapter 6. '''

def drop(inventory):
    itemToDrop = input("Which item do you want to drop?\n\t")
    while True:
        if itemToDrop in inventory:
            inventory.remove(itemToDrop)
            print(f"{itemToDrop} was dropped from the inventory.")
            break
        else:
            print("Item not in inventory. Look at list and try again.")

def main():
    welcome()
    
    inventory = readInventory()
    
    returnToCommand = "y"
    while returnToCommand == "y":
        commandMenuSelection = commandMenu()
        
        if commandMenuSelection.lower() == "show":
            show(inventory)
        elif commandMenuSelection.lower() == "walk":
            walk(inventory)
        elif commandMenuSelection.lower() == "drop":
            drop(inventory)
        elif commandMenuSelection.lower() == "exit":
            break
        
        returnToCommand = input("Return to Command Menu? (y/n) n = exit\n")

    print("later")

if __name__ == "__main__":
    main()