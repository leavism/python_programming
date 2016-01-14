# 6.2 Defining a function
''' def functionName(list of parameters)
		function body
'''

# 6.3 Calling a Function
''' To use a function, you have to call or invoke it. 
If the function returns a value,  a call to that function is usually treated as a value. For example:

	larger = max(3, 4)

larger calls mac(3, 4) and assigns the result of the function to the variable larger.

	print(max(3, 4))

this preints the return value of the function call max(3, 4)
'''

	# Return th emax of two numbers
def max(num1, num2):
	if num1 > num2:
			result = num1
	else:
		result = num2
	return result

def main():
	i = 5
	j =2
	k = max(i, j) # Call the max function
	print("The lager number of",i,"and",j,"is",k)

main()

''' Results:
The lager number of 5 and 2 is 5
'''

# 6.4 Runctions wiht/without Return Values

''' Functions that do not return a value are known as void functions'''

	# print grade for the score
def printGrade(score):
	if score >= 90.0:
		print("A")
	elif score >= 80.0:
		print("B")
	elif score >= 70.0:
		print("C")
	elif score >= 60.0:
		print("C")
	else:
		print("F")

def main():
	score = eval(input("Enter a score: "))
	print("The grade is ", end = "")
	printGrade(score)

main()

''' Results:
Enter a score: 78.5
The grade is C
'''

''' Sometimes, a return statement is used for terminating the function and returning control to the function's caller.
'''

def printGrade(score):
	if score < 0 or score > 100:
		print("Invalid score")
		return # Terminates function cause the input score is invalid, no longer needing to run the rest of the function
	if score >= 90.0:
		print("A")
	elif score >= 80.0:
		print("B")
	elif score >= 70.0:
		print("C")
	elif score >= 60.0:
		print("C")
	else:
		print("F")

def main():
	score = eval(input("Enter a score: "))
	print("The grade is ", end = "")
	printGrade(score)

main()

# Positional and Keyword Arguments
