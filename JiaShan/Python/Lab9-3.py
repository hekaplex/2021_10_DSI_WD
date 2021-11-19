'''
Create a program that displays a report of sales by quarter for a company with four sales
regions (Region 1, Region 2, Region 3, and Region 4).
Console

Sales Report
Region Q1 Q2 Q3 Q4
1 $1,540.00 $2,010.00 $2,450.00 $1,845.00
2 $1,130.00 $1,168.00 $1,847.00 $1,491.00
3 $1,580.00 $2,305.00 $2,710.00 $1,284.00
4 $1,105.00 $4,102.00 $2,391.00 $1,576.00
Sales by region:
Region 1: $7,845.00
Region 2: $5,636.00
Region 3: $7,879.00
Region 4: $9,174.00
Sales by quarter:
Q1: $5,355.00
Q2: $9,585.00
Q3: $9,398.00
Q4: $6,196.00
Total annual sales, all regions: $30,534.00

Specifications
 The quarterly sales numbers for each region should be hard-coded at the beginning of
the program as a list of lists like this:
sales = [[1540.0, 2010.0, 2450.0, 1845.0], # Region 1
[1130.0, 1168.0, 1847.0, 1491.0], # Region 2
[1580.0, 2305.0, 2710.0, 1284.0], # Region 3
[1105.0, 4102.0, 2391.0, 1576.0]] # Region 4
'''

sales = [[1540.0, 2010.0, 2450.0, 1845.0], # Region 1
[1130.0, 1168.0, 1847.0, 1491.0], # Region 2
[1580.0, 2305.0, 2710.0, 1284.0], # Region 3
[1105.0, 4102.0, 2391.0, 1576.0]] # Region 4
import math as m
print('Sales Report\nRegion Q1 Q2 Q3 Q4')
for i, reg in enumerate(sales, start=1):
    print(f'{i}. {reg}')
