'''
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
def display_title():
    print("Prime Number Checker")
    print()

def get_valid_int():
    while True:
        num = int(input("Please enter an integer between 1 and 5000: "))
        if num <= 1 or num >= 5000:
            print("Invalid integer. Please try again.")
        else:
            return num

def get_factor_count(num):
    factor_count = 0
    factors = []
    for i in range(1, num+1):
        remainder = num % i
        if remainder == 0:
            factor_count +=1
    return factor_count

def get_factors(num):
    factors = []
    for i in range(1, num+1):
        remainder = num % i
        if remainder == 0:
            factors.append(i)
    return factors

def main():
    display_title()
    
    again = 'y'
    while again == 'y':
        num = get_valid_int()
        factor_count = get_factor_count(num)
        factors = get_factors(num)
        if factor_count == 2:
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is NOT a prime number.")
            print(f"It has {factor_count} factors.:", end=" ")
            for i in factors:
                print(i, end=" ")            
        print()
        again = input("Try again? (y/n): ")
        print()
        
    print("Bye!")

if __name__ == "__main__":
    main()