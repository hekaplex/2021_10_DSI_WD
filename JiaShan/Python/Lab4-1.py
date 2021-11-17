'''
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

def evenoddchecker(intnumber):
    if intnumber%2 == 0:
        print('This is an even number')
    else:
        print('This is an odd number')
def main():
    print('Even or Odd Checker')
    intnumber = int(input('Enter an integer: '))
    return evenoddchecker(intnumber)
if __name__ == "__main__":
    main()

