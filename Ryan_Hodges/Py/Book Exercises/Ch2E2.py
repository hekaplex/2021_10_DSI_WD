'''
Project 2-2: Pay Check Calculator
Create a program that calculates a user’s weekly gross and take-home pay.
Console
Pay Check Calculator
Hours Worked:       35
Hourly Pay Rate:    14.50

Gross Pay:          507.5
Tax Rate:           18%
Tax Amount:         91.35
Take Home Pay:      416.15

Specifications
 The formula for calculating gross pay is:
gross pay = hours worked * hourly rate
 The formula for calculating tax amount is:
tax amount = gross pay * (tax rate / 100)
 The formula for calculating take home pay is:
take home pay = gross pay – tax amount
 The tax rate should be 18%, but the program should store the tax rate in a variable so
you can easily change the tax rate later just by changing the value that’s stored in the
variable.
 The program should accept decimal entries like 35.5 and 14.25.
 Assume the user will enter valid data.
 The program should round the results to a maximum of two decimal places.
'''

hoursWorked = float(input("How many hours did you work? "))
hourlyPayRate = float(input("How much do you make per hour? "))
grossPay = hoursWorked*hourlyPayRate
taxRate = .18
taxAmount = grossPay*taxRate

print("\nGross Pay: \t" + str(grossPay))
print("Tax Rate: \t" + str(int(taxRate*100)) + "%")
print("Tax Amount: \t" + str(grossPay*taxRate))
print("Take Home Pay: \t" + str(grossPay-taxAmount))