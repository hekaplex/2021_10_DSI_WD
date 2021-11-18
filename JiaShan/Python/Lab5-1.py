TAX = 0.06

def sales_tax(total):
    sales_tax = total * TAX
    return sales_tax

def main():
    print("Sales Tax Calculator\n")
    total = float(input("Enter total: "))
    total_after_tax = total + sales_tax(total)
    print("Total after tax: ", total_after_tax)
    
if __name__ == "__main__":
    main()
'''
TAX = 0.06

def sales_tax(total) #missing :
    sales_tax = total * tax #should be TAX
    return total # should return sales_tax

def main():
    print("Sales Tax Calculator\n")
    total = float(input("Enter total: "))
    total_after_tax = round(total + sales_tax(total), 2)
    print("Total after tax: ", total_after_tax)
    
if __name__ == "__main__":
    main()
'''