SALESTAXRATE = .06


def title():
    print("Sales Tax Calculator")

def receiptMaker():
    subtotal = 0
    costOfItem = round(float(input("Cost of item: ")),2)
    subtotal += costOfItem
    while costOfItem != 0:
        costOfItem = round(float(input("Cost of item: ")),2)
        subtotal += costOfItem
    return subtotal

def salesTaxRate(subTotal):
    salesTax = round(float(subTotal*SALESTAXRATE),2)
    return salesTax

def totalSaleWithTax(subTotal, salesTax):
    totalSale = round(float(subTotal+salesTax),2)
    return totalSale

def main():
    title()

    newReceipt = ("y")
    
    while newReceipt.lower() == "y":
        print("ENTER ITEMS (ENTER 0 TO END)")
        subTotal = round(receiptMaker(),2)
        print("Sub-total: \t" + str(subTotal))
        salesTax = round(salesTaxRate(subTotal),2)
        print("Sales Tax: \t" + str(round(salesTax,2)))
        totalSale = round(float(totalSaleWithTax(subTotal,salesTax)),2)
        print("Total Sales: \t" + str(round(totalSale,2)))
        newReceipt = input("Would you like a new receipt? (y/n) ")
    
    print("later")

if __name__ == "__main__":
    main()