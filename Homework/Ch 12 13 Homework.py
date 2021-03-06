# 12.1
'''
from GeometricObject import GeometricObject
import math

class Triangle(GeometricObject):
    def __init__(self, side1 = 1.0, side2 = 1.0, side3 = 1.0):
        super().__init__()
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3
    def getSide1(self):
        return self.__side1
    def setSide1(self, side1):
        self.__side1 = side1
    def getSide2(self):
        return self.__side2
    def setSide2(self, side2):
        self.__side2 = side2
    def getSide3(self):
        return self.__side3
    def setSide3(self, side3):
        self.__side3 = side3
    def getArea(self):
        s = (self.__side1 + self.__side2 + self.__side3) / 2
        return (s * (s - self.__side1) * (s - self.__side2) * (s - self.__side3) ** 0.5)
    def getPerimeter(self):
        return self.__side1 + self.__side2 + self.__side3
    def __str__(self):
        return "Triangle: side1 = " + str(self.__side1) + " side2 = " + str(self.__side2) + " side3 = " + str(self.__side3)

def main():
    s1 = eval(input("Enter measurement of side 1: "))
    s2 = eval(input("Enter measurement of side 2: "))
    s3 = eval(input("Enter measurement of side 4: "))
    c = input("Enter the color: ")
    f = eval(input("Is it filled? Enter 1 for yes, 0 for no: "))
    triangle = Triangle(s1, s2, s3)
    print(triangle)
    print("The area is", triangle.getArea())
    print("The perimeter is", triangle.getPerimeter())
    tg = GeometricObject(c, bool(f))
    print("The color is", tg.getColor())
    print("Filled: ", tg.isFilled())
main()

 Results:
Enter measurement of side 1: 3
Enter measurement of side 2: 4
Enter measurement of side 4: 5
Enter the color: yellow
Is it filled? Enter 1 for yes, 0 for no0
Triangle: side1 = 3 side2 = 4 side3 = 5
The area is 36.0
The perimeter is 12
The color is yellow
Filled? False

Enter measurement of side 1: 4
Enter measurement of side 2: 5
Enter measurement of side 4: 6
Enter the color: brown
Is it filled? Enter 1 for yes, 0 for no: 0
Triangle: side1 = 4 side2 = 5 side3 = 6
The area is 80.37388218507303
The perimeter is 15
The color is brown
Filled? False
'''

# 12.3

from account import account

for i in range (10):
    accountlist = []
    accountlist.append(account(id = i))


class atm(account):
    def __init__(self, id):
        super().__init__()
        self.__id = id
    def mainMenu(self):
        return "Main menu \n1: Check balance \n2: Withdraw \n3: Deposit \n4: Exit"

        

def main1():
    idInput = eval(input("Input your ID: "))
    atmSim = atm(idInput)
    print(atmSim.mainMenu())
    choiceInput = eval(input("Enter a choice:" ))
    if choiceInput == 1:
        print(atmSim.getBalance())
        main1()
    elif choiceInput == 2:
        d = eval(input("Enter amount to withdraw: "))
        atmSim.withdraw(d)
        main1()
    else:
        None

main1()



# 13.3
'''
from random import randint

# Makes the unspecified number of scores
def makeScores():
    num = randint(0, 25)
    outfile = open("scores.txt", "w")
    for i in range(num):
        outfile.write(str(randint(0, 9)) + " ")
    outfile.close()

def processScores():
    nameFile = input("Enter a filename: ")
    infile = open(str(nameFile), "r")
    s = infile.read()
    numbers = [eval(x) for x in s.split()]
    i = 0
    ssplitted = s.split()
    for number in numbers:
        i += 1
    print("There are",i,"scores")


    b = sum(numbers)
    print("The total is ", b)

    average = b / i
    print("The average is",average)
    infile.close()
makeScores()
processScores()
'''
''' Results:
Enter a filename: scores.txt
There are 23 scores
The total is  99
The average is 4.304347826086956
'''
