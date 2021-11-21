from datetime import datetime

halloween = datetime.strptime("10/31/1988", "%m/%d/%Y")

print(halloween)

halloween = datetime.strptime("31-10-1988", "%d-%m-%Y")

print(halloween)

halloween = datetime.strptime("10/31/1988 22:30", 
                              "%m/%d/%Y %H:%M")
print(halloween)
