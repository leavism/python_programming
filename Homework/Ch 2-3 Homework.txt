''' Ch2, Ch3 Homework
Helen Sun 1/4/2016
Giahuy Dang
'''
# Exercise 2.5
subtotal, gratuity = eval(input("Enter the subtotal and a grauity rate: "))
gratuity_calc = subtotal * (gratuity / 100)
subtotal_calc = subtotal + gratuity_calc
print("The gratuity is ",gratuity_calc,"and the total is",subtotal_calc)

Results:
Enter the subtotal and a grauity rate: 15.69, 15
The gratuity is  2.3535 and the total is 18.043499999999998

# Exercise 2.13
integer = eval(input("Enter an integer: "))
d1 = integer // 1000
n2 = integer % 1000
d2 = n2 // 100
n3 = integer % 100
d3 = n3 // 10
n4 = integer % 10
d4 = n4
print(d1)
print(d2)
print(d3)
print(d4)

'''
Results:
Enter an integer: 6542
6
5
4
2
'''

# Exercise 2.15
sides = eval(input("Enter the side:"))
area = ((3 * 1.732050807568877)/(2)) * sides**2
print("The area of the hexagon is ", area)

''' Results:
Enter the side:79
The area of the hexagon is  16214.593635056042
'''

# Exercise 3.9
name = input("Enter employee's name: ")
hours_worked = eval(input("Enter number of hours worked in a week: "))
hourly_pay = eval(input("Enter hourly pay rate: "))
input_federal_tax_withholding = eval(input("Enter federal tax withhoulding rate: "))
input_state_tax_withholding = eval(input("Enter state tax withholding rate: "))
federal_tax_withholding = input_federal_tax_withholding * 100
state_tax_withholding = input_state_tax_withholding * 100

print("Employee Name: Smith \nHours worked:", format(hours_worked, ".1f"), "\nPay Rate: $",hourly_pay, "\nGross Pay: $",hourly_pay * 10, \
      "\nDeductions: \n  Federal Withholding (",federal_tax_withholding,"%): $",(hourly_pay / 10) * federal_tax_withholding, \
      "\n  State Withholding (",state_tax_withholding,"%): $",format((hourly_pay / 10) * state_tax_withholding,"<.2f"), \
      "\n  Total Deduction: $",format((hourly_pay / 10) * federal_tax_withholding + (hourly_pay / 10) *state_tax_withholding,"<.2f"), \
      "\nNet Pay: $",format((hourly_pay* 10) - ((hourly_pay / 10) * federal_tax_withholding + (hourly_pay / 10) *state_tax_withholding),".2f"))

''' Results:
Enter employee's name: Smith
Enter number of hours worked in a week: 10
Enter hourly pay rate: 9.75
Enter federal tax withhoulding rate: 0.20
Enter state tax withholding rate: 0.09
Employee Name: Smith 
Hours worked: 10.0 
Pay Rate: $ 9.75 
Gross Pay: $ 97.5 
Deductions: 
  Federal Withholding ( 20.0 %): $ 19.5 
  State Withholding ( 9.0 %): $ 8.78 
  Total Deduction: $ 28.27 
Net Pay: $ 69.22
'''

# Exercise 3.11
integer = eval(input("Enter an integer: "))
d1 = integer // 1000
n2 = integer % 1000
d2 = n2 // 100
n3 = integer % 100
d3 = n3 // 10
n4 = integer % 10
d4 = n4
print(d4, end = '')
print(d3, end = '')
print(d2, end = '')
print(d1, end = '')

''' Results:
Enter an integer: 6542
2456
'''
