# 5.1 Introduction

'''
The variable count is initially at 0. The while loop checks whether count < 10 is true. If so, it executes the loop body, printing
"Progamming is fun!" and increments count by 1. It does this until count < 10 is false.
'''
count = 0
while count < 10:
	print("Programming is fun!")
	count += 1

# 5.2 The while Loop
'''
The syntax for the while loops is:
	while loop-continuation-condition:
		loop body
		statement(s)

If i < 10 is true, program adds i to sum. The variable i is initially 1, then increments to 2,3,4,5,6,7,8,9,10. When i is 10, i < 10
is false and the loop exits. Every increment of i is then added to sum. In the end, sum = 45
'''
sum = 0
i = 1
while i < 10:
	sum += i
	i += 1
print("sum is",sum)

''' Example '''
import random

	# 1. Generate two random single-digit integers
number1 = random.randint(0,9)
number2 = random.randint(0,9)

	# 2. If number1 < number2, swap number1 with number2
if number1 < number2:
	number1, number2 = number2, number1
	# 3. Prompt user to answer "What is number1 - number2?"
answer = eval(input("What is " + str(number1) + "-" + str(number2) + "? "))
	#Ask question until the answer is correct
while number1 - number2 != answer:
	answer = eval(input("Wrong answer. Try again. What is "+ str(number1) + " - " + str(number2) + "? "))

	# 5.2.4 Controlling a Loop with User Confirmation
continueLoop = "Y"
while continueLoop == "Y":
	continueLoop = input("Enter Y to continue and N to quite: ")
# 5.3 The for Loop
	'''Often you know exactly how many times the loop body needs to be executed, so a control variable can be used to
 	count the executions.

 	for i in range(initialValue, endValue):
 		Loop body

 	In general, the syntax of a for loop is:

 	for var in sequence:
 		loop body
 	'''

for v in range(4, 8):
	print(v)
''' Prints variable v, which is every number between 4 and 8. Including 4, not including 8 
Results: 
4
5
6
7
'''

for v in range(3, 9, 2):
	print(v)
''' Prints variable v, which is every number between 3, 9 at the step value of two.
Results:
3
5
7
'''

# Keywords break and continue
'''You can use the keyword break in a loop to immediately terminate  loop.'''

sum = 0
number = 0

while number < 20:
	number += 1
	sum += number
	if sum >= 100:
		break
print("The number is", number)
print("The sum is", sum)
''' You can use the keyboard continue, it ends the current iteration and program control goes to the end of the loop body.'''
sum = 0
number = 0

while number < 20:
	number += 1
	if number == 10 or number == 11:
		continue
	sum += number
print("The sum is", sum)