'''Project 4-5: Dice Roller 
Create a program that uses a function to simulate the roll of a die.
Console 
Dice Roller 
Roll the dice? (y/n): y
Die 1: 3 
Die 2: 6 
Total: 9 
Roll again? (y/n): y
Die 1: 1 
Die 2: 1 
Total: 2 
Snake eyes! 
Roll again? (y/n): y
Die 1: 6 
Die 2: 6 
Total: 12 
Boxcars! 
Roll again? (y/n): n
Specifications 
 The program should roll two six-sided dice. 
 Store the code that rolls a single die in a function. 
 Store the code that gets input and displays output in the main() function. Divide this 
code into functions whenever you think it would make that code easier to read and 
maintain. 
 The program should display a special message for two ones (snake eyes) and two 
sixes (boxcars).'''

import random

def welcome():
    print("Dice Roller")
    print()

def rollDice():
    rollChoice = input("Would you like to roll the dice? (y/n) ")
    while rollChoice == "y":
        randomNumber1 = random.randint(1,6)
        randomNumber2 = random.randint(1,6)
        print("Die 1: " + str(randomNumber1))
        print("Die 2: " + str(randomNumber2))
        print("Total: " + str(randomNumber1+randomNumber2))
        if randomNumber1 == 1 and randomNumber2 == 1:
            print("Snake eyes!")
        elif randomNumber1 == 6 and randomNumber2 == 6:
            print("Boxcars!")
        rollChoice = input("Would you like to roll again? (y/n) ")
    

def main():
    welcome()

    rollDice()

    print("Bye")

if __name__ == "__main__":
    main()