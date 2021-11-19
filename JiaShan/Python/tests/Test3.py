''''''
''''''
'''
number = input("Enter an integer: ")
if type(number) is int:
    n = int(number)
    print(f"You entered a valid integer of {number}.")
else:
    print("Please provide an integer")
    number = input("Enter an integer: ")
'''
'''
def putint():
'''


while True:
    try:
        number = int(input("Enter an integer: "))
        print(f"You entered a valid integer of {number}.")
        break
    except ValueError:
            print("You entered an invalid integer. Please try again.")
print("Thanks!")
'''
def main():
    putint()
    
if __name__ == "__main__":
    main()

'''

