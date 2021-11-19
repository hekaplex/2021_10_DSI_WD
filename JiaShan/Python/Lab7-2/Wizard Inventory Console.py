ALLINVENTORY = "C:\\Users\\jiash\\Desktop\\DSI DATA\\2021_10_DSI_WD\\2021_10_DSI_WD\\JiaShan\\Python\\Lab7-2\\wizard_all_items.txt"

CURINVENTORY = "C:\\Users\\jiash\\Desktop\\DSI DATA\\2021_10_DSI_WD\\2021_10_DSI_WD\\JiaShan\\Python\\Lab7-2\\wizard_inventory.txt"

import random

def display():
    print('The Wizard Inventory program\nCOMMAND MENU\nwalk - Walk down the path\nshow - Show all items\ndrop - Drop an item\nexit - Exit program')
    
def walk():
    runintoitem =[]
    for n in ALLINVENTORY:
            runintoitem.append(n)
            for l in CURINVENTORY:
                runintoitem.remove(l)
                return random.choice({runintoitem}) 
    
def inventorylist():
    for i, item in enumerate(CURINVENTORY, start=1):
        print(f'{i}. {item}')

def add():
    grabornot = 'y'
    grabornot = input('Do you want to grab it? (y/n): ')
    while grabornot == 'y':
        CURINVENTORY.append(walk())
        if len(CURINVENTORY) < 5:
            print(f'You picked up {walk()}')
            break
        else:
            print(f"You can't carry any more items. Drop something first.")
            return

def delete():
    pick = int(input('Number: '))
    if pick < 1 or pick > len(CURINVENTORY):
        print("Invalid number, please check inventory number")
    else:        
        whatwelost = CURINVENTORY.pop(pick-1)
        print(f"You dropped {whatwelost}")

def main():

    display()
    while True:
        command = input('Command: ')
        if command == 'walk':
            walk()
            if command == 'add':
                add()
        elif command == 'show':
            inventorylist
        elif command == 'drop':
            delete()
        elif command == 'exit':
            break
        else:
            print('You have to walk before grad or provide a valid command from the menu')
    print("Bye!")
    
if __name__ == "__main__":
    main()