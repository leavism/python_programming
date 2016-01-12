''' Ch1 Homework
Helen Sun 1/4/2016
Giahuy Dang
'''
 
# Exercise 1.4
print("a  a^2 a^3 \n1  1   1 \n2  4   8 \n3  9   27 \n4  16  64")

''' Results:
a  a^2 a^3 
1  1   1 
2  4   8 
3  9   27 
4  16  64
'''

# Exercise 1.9
width = 4.5
height = 7.9
area = width * height
perimeter = 2 * width + 2 * height

print("The area of the rectangle is",area,", while the perimeter is ",perimeter)

''' Results:
The area of the rectangle is 35.550000000000004 , while the perimeter is  24.8
'''

# Exercise 1.15
import turtle

turtle.pencolor("Blue")
turtle.pendown()
turtle.right(45)
turtle.forward(75)

turtle.right(135)
turtle.forward(105)

turtle.right(135)
turtle.forward(150)

turtle.left(135)
turtle.forward(105)

turtle.left(135)
turtle.forward(75)

turtle.done()

# Execise 1.11
init_population = 312032486
day = 86400
year = day * 365
pop_calc = + (year // 7) - (year // 13) + (year // 45)
year1 = init_population + pop_calc
year2 = year1 + pop_calc
year3 = year2 + pop_calc
year4 = year3 + pop_calc
year5 = year4 + pop_calc
print("The population after one year is",year1,".")
print("The population after two years is",year2,".")
print("The population after three years is",year3,".")
print("The population after four years is",year4,".")
print("The population after five years is",year5,".")

'''Results
The population after one year is 314812582 .
The population after two years is 317592678 .
The population after three years is 320372774 .
The population after four years is 323152870 .
The population after five years is 325932966 .
'''
