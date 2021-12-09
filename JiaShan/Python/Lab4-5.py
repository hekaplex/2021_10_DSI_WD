'''
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
sixes (boxcars).
'''
import random as r
def die1():
    die1 = r.randint(1,6)
    return int(die1)
def die2():
    die2 = r.randint(1,6)
    return int(die2)
def main():
    print('Dice Roller')
    choice = 'y'
    choice = input('Roll the dice?: (y/n): ')
    while choice == 'y':
        roll = 'y'
        while roll == 'y':
            total =die1()+die2()
            if total == 2:
                print(f'Die1: {die1()}\nDie2: {die2()}\nTotal: {total}\Snake eyes!')
            elif total == 12:
                print(f'Die1: {die1()}\nDie2: {die2()}\nTotal: {total}\Boxcars!')
            else:
                print(f'Die1: {die1()}\nDie2: {die2()}\nTotal: {total}')
            roll = input('Roll again? (y/n):')
        break
    print('Thank you for playing')
if __name__ == "__main__":
    main()