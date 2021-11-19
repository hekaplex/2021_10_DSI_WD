'''#!/usr/bin/env python3

TAX = 0.06

def sales_tax(total)
    sales_tax = total * tax
    return total

def main():
    print("Sales Tax Calculator\n")
    total = float(input("Enter total: "))
    total_after_tax = round(total + sales_tax(total), 2)
    print("Total after tax: ", total_after_tax)
    
if __name__ == "__main__":
    main()
'''
'''
sales_tax: missing colon
tax (inside sales_tax) should be uppercase

'''
#!/usr/bin/env python3

TAX = 0.06

def sales_tax(total):
    sales_tax = total * TAX
    return total

def main():
    print("Sales Tax Calculator\n")
    total = float(input("Enter total: "))
    total_after_tax = round(total + sales_tax(total), 2)
    print("Total after tax: ", total_after_tax)
    
if __name__ == "__main__":
    main()
