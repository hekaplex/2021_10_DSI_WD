'''
Project 4-1: Even or Odd Checker
Create a program that checks whether a number is even or odd.
Console
Even or Odd Checker
Enter an integer: 33
This is an odd number.
Specifications
 Store the code that gets user input and displays output in the main() function.
 Store the code that checks whether the number is even or odd in a separate function.
 Assume that the user will enter a valid integer.
'''


def is_Odd(num):
    if float(num%2)==1:
        return True
    else:
        return False
    
def main():
    print("Even or Odd Checker")
    numberCheck = int(input("Enter an integer. "))
    if is_Odd(numberCheck):
        print("Your number is odd.")
    else:
        print("Your number is even.")

if __name__ == "__main__":
    main()


'''
# the add function
def is_even(num):
    print("Inside is_even function")
    print(num)
    if num % 2 == 0:
        return True
    else:
        return False

# the main function
def main():
    print("Even or Odd Checker")
    print("\n")
    my_num = int(input("Enter an integer:  "))
    if is_even(my_num):
        print("This is an even number.")
    else:
        print("This is an odd number.")

if __name__ == "__main__":
    main()'''