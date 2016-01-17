
# Exercise 7.1
from rectangle import rectangle

def main():
	rect1 = rectangle(4,40)
	print("The area of a rectangle with the width of",rect1.getWidth(),"and height of",rect1.getHeight(),"is",rect1.getArea(),"and the perimeter is",rect1.getPerimeter())
	rect2 = rectangle(3.5, 35.7)
	print("The area of a rectangle with the width of",rect2.getWidth(),"and height of",rect2.getHeight(),"is",rect2.getArea(),"and the perieter is",rect2.getPerimeter())

main()

''' Results:
The area of a rectangle with the width of 4 and height of 40 is 160 and the perimeter is 88
The area of a rectangle with the width of 3.5 and height of 35.7 is 124.95000000000002 and the perieter is 78.4
'''

# Exercise 7.3
from account import account

def creator():
	creator1 = account()
	creator1.setId(1122)
	creator1.setBalance(20000)
	creator1.setAnnualInterestRate(45)
	creator1.deposit(3000)

	print("ID: ",creator1.getId())
	print("Balance: ",creator1.getBalance())
	print("Annual Interest Rate: ",creator1.getAnnualInterestRate())
	print("Monthly Interest Rate: ",creator1.getMonthlyInterestRate())
	print("Monthly Interest: ",creator1.getMonthlyInterest())
creator()

'''Results:
ID:  1122
Traceback (most recent call last):
Balance:  23000
Annual Interest Rate:  0.045
Monthly Interest Rate:  0.00375
Monthly Interest:  86.25
'''

# Exercise 8.4
def count(s, ch):
	n  = 0 
	for i in s:
		if i == ch:
			n += 1
	print(n)

string = input("Enter a string: ").strip()
search = input("Enter a character: ").strip()

count(string, search)

''' Results:
Enter a string: asdfaaa
Enter a character: a
4
'''

