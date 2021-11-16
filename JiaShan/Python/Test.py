miles_driven = int(input('Enter the miles driven in integer:'))
fuel_used = float(input('Enter fuel used in float:'))
mpg = round(miles_driven/fuel_used,2)
print('Your vehicle MPG is:'+str(mpg))