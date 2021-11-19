'''
Project 6-1: Prime Number Checker 
Create a program that checks whether a number is a prime number and displays its 
factors if it is not a prime number. 
Console 
Prime Number Checker 
Please enter an integer between 1 and 5000: 5
5 is a prime number. 
Try again? (y/n): y
Please enter an integer between 1 and 5000: 6
6 is NOT a prime number. 
It has 4 factors: 1 2 3 6 
Try again? (y/n): y
Please enter an integer between 1 and 5000: 200
200 is NOT a prime number. 
It has 12 factors: 1 2 4 5 8 10 20 25 40 50 100 200 
Try again? (y/n): n
Bye! 
Specifications 
 A prime number is divisible by two factors (1 and itself). For example, 7 is a prime 
number because it is only divisible by 1 and 7. 
 If the user enters an integer that’s not between 1 and 5000, the program should 
display an error message. 
 If the number is a prime number, the program should display a message to that effect. 
 If the number is not a prime number, the program should display a message to that 
effect. Then, it should display the number of factors for the number and a list of those 
factors. 
 Store the factors for each number in a list. 
 Use functions to organize the code for this program.
'''

def welcome():
    print("Prime Number Checker")

def validityTester():
    testedNumber = int(input("Please enter a number between 1 and 5000: "))
    while testedNumber <= 1 or testedNumber >= 5000:
        testedNumber = int(input("Invalid integer.  Enter a number between 1 and 5000: "))
    return testedNumber
    
def primeTester(testedNumber):
    factorList = []
    for i in range(1, testedNumber+1):
        remainder = testedNumber % i
        if remainder == 0:
            factorList.append(i) 
    return factorList
        
def main():
    welcome()

    tryAgain = "y"
    while tryAgain == "y":

        testedNumber = validityTester()
        factorList = primeTester(testedNumber)
        factorCounter = len(factorList)
        if factorCounter == 2:
            print(f"{testedNumber} is a prime number!")
            print(factorList)
        else:
            print(f"{testedNumber} is not a prime number.\n")
            print(f"Your number has {factorCounter} factors")
            print(factorList)
                    
        tryAgain = input("\nWould you like to try again? (y/n) ")

    print("Bye")

if __name__ == "__main__":
    main()