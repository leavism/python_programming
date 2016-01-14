# Exercise 6.9
# Feet to meters module:

from feettometer import footToMeter
from metertofoot import meterToFoot

print("Feet     Meters      |     Meters     Feet")
print("1.0      ",format(footToMeter(1.0),"<10.3"),"|     20.0      ",format(meterToFoot(20.0),"<10.3f"))
print("2.0      ",format(footToMeter(2.0),"<10.3"),"|     26.0      ",format(meterToFoot(26.0),"<10.3f"))
print("3.0      ",format(footToMeter(3.0),"<10.3"),"|     30.0      ",format(meterToFoot(30.0),"<10.3f"))
print("4.0      ",format(footToMeter(4.0),"<10.3"),"|     36.0      ",format(meterToFoot(36.0),"<10.3f"))
print("5.0      ",format(footToMeter(5.0),"<10.3"),"|     40.0      ",format(meterToFoot(40.0),"<10.3f"))
print("6.0      ",format(footToMeter(6.0),"<10.3"),"|     46.0      ",format(meterToFoot(46.0),"<10.3f"))
print("7.0      ",format(footToMeter(7.0),"<10.3"),"|     50.0      ",format(meterToFoot(50.0),"<10.3f"))
print("8.0      ",format(footToMeter(8.0),"<10.3"),"|     56.0      ",format(meterToFoot(56.0),"<10.3f"))
print("9.0      ",format(footToMeter(9.0),"<10.3"),"|     60.0      ",format(meterToFoot(60.0),"<10.3f"))
print("10.0     ",format(footToMeter(10.0),"<10.3"),"|     66.0      ",format(meterToFoot(66.0),"<10.3f"))

'''
Results:
Feet     Meters      |     Meters     Feet
1.0       0.305      |     20.0       65.574    
2.0       0.61       |     26.0       85.246    
3.0       0.915      |     30.0       98.361    
4.0       1.22       |     36.0       118.033   
5.0       1.52       |     40.0       131.148   
6.0       1.83       |     46.0       150.820   
7.0       2.13       |     50.0       163.934   
8.0       2.44       |     56.0       183.607   
9.0       2.75       |     60.0       196.721   
10.0      3.05       |     66.0       216.393   
'''
# Exercise 6.11

def computerCommission(n):
	if n <= 5000:
		c = n * 0.08
		return c
	elif n > 5000 and n <= 10000:
		c = (5000 * 0.08) + ((n - 5000) * 0.1)
		return c
	elif n > 10000:
		c =  (5000 * 0.08) + (5000 * 0.1) + ((n - 10000) * 0.12)
		return c


print("Sales Amount          Commission")
for n in range(10000, 100000, 5000):
	print(n,"               ",format(computerCommission(n),"10.1f"))
print("100000               ",format(computerCommission(100000),"10.1f"))

'''
 Results:

Sales Amount          Commission
10000                      900.0
15000                     1500.0
20000                     2100.0
25000                     2700.0
30000                     3300.0
35000                     3900.0
40000                     4500.0
45000                     5100.0
50000                     5700.0
55000                     6300.0
60000                     6900.0
65000                     7500.0
70000                     8100.0
75000                     8700.0
80000                     9300.0
85000                     9900.0
90000                    10500.0
95000                    11100.0
100000                   11700.0
'''

# Exercise 6.18

import random

z = eval(input("Enter n: "))
def printMatrix(n):
	column = n
	row = n
	for k in range(0, n):
		for i in range(1, column + 1):
			print(random.randint(0,1), end = " ")
		if (i) % row == 0:
			print()

printMatrix(z)

'''
Results:

Enter n: 7
0 0 0 0 0 0 0 
0 0 0 0 0 0 0 
1 1 1 0 1 0 0 
1 0 1 0 1 1 0 
1 0 1 1 0 0 0 
1 1 0 0 1 1 1 
1 0 1 0 0 0 1

'''
