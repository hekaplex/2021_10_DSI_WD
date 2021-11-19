
def welcome():
    print("\nThe Wizard Inventory Program")

def commandMenu():
    print("\nCOMMAND MENU")
    print("\nshow - Shows all items")
    print("grab - Grabs an item")
    print("edit - Edits an item")
    print("drop - Drops an item")
    print("exit - Exits program")
    commandSelection = input("\nType name of action to take.\n")
    return commandSelection

def show(inventory):
    for i, item in enumerate(inventory, start=1):
        print(f"{i}. {item}")
    print()

def grab(inventory):
    itemToGrab = input("What are you grabbing?\n\t")
    if len(inventory) <= 3:
        inventory.append(itemToGrab)
    else:
        print("Inventory is full.  You must drop an item in order to gain a new one.")

def edit(inventory):
    itemToEdit = input("Which item do you want to edit?\n\t")
    itemEditIndex = inventory.index(itemToEdit)
    inventory.remove(itemToEdit) 
    inventory.insert(itemEditIndex,input("Enter new name for item:\n\t"))

def drop(inventory):
    itemToDrop = input("Which item do you want to drop?\n\t")
    if itemToDrop in inventory:
        inventory.remove(itemToDrop)
        print(f"{itemToDrop} was dropped from the inventory.")
    else:
        print("Item not in inventory. Look at list and try again.")

def main():
    welcome()
    inventory4Slots = ["Funny Hat","Man-jams","Curly Shoes"]
    
    returnToCommand = "y"
    while returnToCommand == "y":
        commandMenuSelection = commandMenu()
        
        if commandMenuSelection.lower() == "show":
            show(inventory4Slots)
        elif commandMenuSelection.lower() == "grab":
            grab(inventory4Slots)
        elif commandMenuSelection.lower() == "edit":
            edit(inventory4Slots)
        elif commandMenuSelection == "drop":
            drop(inventory4Slots)
        elif commandMenuSelection == "exit":
            break
        
        returnToCommand = input("Return to Command Menu? (y/n) n = exit\n")

    print("later")

if __name__ == "__main__":
    main()