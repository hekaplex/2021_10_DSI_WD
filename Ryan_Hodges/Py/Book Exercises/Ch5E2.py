'''#!/usr/bin/env python3

import random

def display_title():
    print("Guess the number!")
    print()

def get_limit():
    limit = int(input("Enter the upper limit for the range of numbers: "))
    return limit

def play_game(limit):
    number = random.randint(1, limit)
    print(f"I'm thinking of a number from 1 to {limit}\n")

    while True:
        guess = int(input("Your guess: "))
        if guess < number:
            print("Too low.")
            count += 1
        elif guess >= number:
            print("Too high.")
            count += 1
        elif guess == number:
            print(f"You guessed it in {count} tries.\n")
            return

def main():
    display_title()
    
    again = "y"
    while again.lower() == "y":
        limit = get_limit()
        play_game()
        
        again = input("Play again? (y/n): ")
        print()
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()
'''
'''
main()
play_game(): guess variable should be outside of while loop
play_game(): too high guess wrong operator
play_game(): if statement does not have else
play_game(): while loop argument does not have a comparison
'''
#!/usr/bin/env python3

import random

def display_title():
    print("Guess the number!")
    print()

def get_limit():
    limit = int(input("Enter the upper limit for the range of numbers: "))
    return limit

def play_game(limit):
    number = random.randint(1, limit)
    print(f"I'm thinking of a number from 1 to {limit}\n")
    
    guess = int(input("Your guess: "))
    inPlay = True
    while inPlay == True:
        
        if guess < number:
            print("Too low.")
            inPlay = True
        elif guess > number:
            print("Too high.")
            inPlay = True
        elif guess == number:
            print(f"You guessed it in {count} tries.\n")
            inPlay = False
            return 

def main():
    display_title()
    
    again = "y"
    while again.lower() == "y":
        limit = get_limit()
        play_game()
        
        again = input("Play again? (y/n): ")
        print()
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()

