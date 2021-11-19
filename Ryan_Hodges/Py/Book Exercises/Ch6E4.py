'''Project 6-4: Quarterly Sales 
Create a program that gets quarterly sales from a user and calculates the total of all four 
quarters as well as the average, lowest, and highest quarters. 
Console 
The Quarterly Sales program 
Enter sales for Q1: 12312.57
Enter sales for Q2: 15293.21
Enter sales for Q3: 14920.95 
Enter sales for Q4: 23432.21
Total: 65958.94 
Average Quarter: 16489.74 
Lowest Quarter: 12312.57 
Highest Quarter: 23432.21 
Specifications 
 Use a list to store the sales for each quarter. 
 Round the results of each entry to a maximum of 2 decimal digits.
'''

def welcome():
    print("The Quarterly Sales Program")

def salesEntry():
    firstQuarter = float(input("Enter sales of Q1: "))
    secondQuarter = float(input("Enter sales of Q2: "))
    thirdQuarter = float(input("Enter sales of Q3: "))
    fourthQuarter = float(input("Enter sales of Q4: "))
    salesByQuarterList = [firstQuarter,secondQuarter,thirdQuarter,fourthQuarter]
    return salesByQuarterList

def main():
    welcome()

    quarterlySales = salesEntry()
    print(f"\nTotal:\t\t" + str(sum(quarterlySales)))
    print(f"Average Quarter: " + str(round((sum(quarterlySales)/len(quarterlySales)),2)))
    print(f"Lowest Quarter: " + str(min(quarterlySales)))
    print(f"Highest Quarter: " + str(max(quarterlySales)))


if __name__ == "__main__":
    main()