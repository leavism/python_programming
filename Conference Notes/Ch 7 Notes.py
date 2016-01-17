# 7.2.1 Defining Classes
'''

A python class uses variables to store data fields and defines methods to perform actions. A class is a contract
that defines what an object's data fields and methods will be.
'''

'''
A class provices a special method, __init__. This method is invoked to initialize a new object's state when it is created. 
An initializer can perform any action, but initializers are designed to perform initializing actions, such as creating an object's data fields
with initial values. 
	Python uses the following syntax to define a class:

	class ClassName
		initilializer
		method
'''

import math

class Circle:
	#Construct a cirlce object
	def __init__(self, radius = 1): #initializer
		self.radius = radius # create data field
	def getPerimeter(self): # getPerimeter() method
		return self.radius * self.radius * math.pi
	def getArea(self): # getArea() method
		return self.radius * self.radius * math.pi
	def setRadius(self, radius):
		self.radius = radius

# 7.2.2 Constructing Objects
'''
Once a class is defined, you can crate objects from the class with a constructor. The constructor does two things:
	1. it creaetes an object in the memory for the class
	2. It invokes the class's __init__ method to initialize the object

All methods, including the initializer, have the first parameter self. This parameter refers to the object that invokes the method.
'''

# 7.2.3 Accessing Members of Objects
'''
AN object's member refers to its data fields and methods. Data fields are also called isntance variables, because each oject (instance) has a
specific value for a data field. 

For example, the following code accesses the radius data field and then invokes the getPerimeter method and the getArea method.
'''

from Circle import Circle
c = Circle(5)
c.radius
''' Results:
5
'''
c.getPerimeter()
''' Results
31.4159265
'''

# 7.2.4 The self parameter
'''
The first parameter for each method defined is self. This parameter is used in the implementation of the method, but it
is not used in the implementation of the method, but it is not used when the method is called.

self is a parameter that references the object itself. Using self, you can access  object's members in a class definition. For example,
you can use the syntax self.x to access the instance variable x and syntax self.m1() to invoke the instance method ml or the object self in a class
'''

def className():
	def __init__(self, ...):
		self.x = 1 # Create/modify x
	def m1(self, ...):
		self.y = 2 # Create/modify y
		z = 5 # Create/modify z
	def m2(self, ...):
		self.y = 3 # create/modify y
		u= self.x + 1 # Create/modify u
		self.m1(...) # invoke m1

''' The scope of an instance variable is the entire class once it is created '''

# 7.2.5 Example: Using Classes

from Circle import Circle

def main():
	# Create a circle with radius 1
	circle1 = circle()
	print("The area of the circle of radius",circle1.radius,"is",circle1.getArea())
	# Create circle with radius 25
	circle2 = circle(25)
	print("The area of the circle of radius",circle2.radius,"is",circle2.getArea())
	circle3 = circle(125)
	print("The area of the circle of radius",circle3.radius,"is",circle3.getArea())

	# Modify circle radius
	circle2.radius = 100 # or circle2.setRadius(100)
	print("The area of the circle of radius",circle2.radius,"is",circle2.getArea())
main() # Call the function

''' Results:
The area of the circle of radius 1.0 is 3.141592653589793
The area of the circle of radius 25.0 is 1963.4954084936207 
The area of the circle of radius 125.0 is 49087.385212340516
The area of the circle of radius 100.0 is 31415.926535897932
'''
# 7.3 UML Class Diagrams

# 7.4 Immutable Objects vs. Mutable Objects
'''
Recall that numbers and strings are immutable objects in Python. Their contents cannot be changed. 
'''

from Circle import Circle
def main():
	# CReate a Circle object with radius 1
	myCircle = Circle()
	# Print areas for radius 1, 2, 3, 4, 5
	n = 5
	printArea(myCircle, n)
	# Display myCircle.radius and times
	print("\nRadius is", myCircle.radius)
	print("n is", n)
# Print a table of areas for radius
def printAreas(c, times):
	print("\Radius \t\tArea")
	while times >= 1:
		print(c.radius, "\t\t", c.getArea())
		c.radius = c.radius + 1
		times = times - 1
main()
''' Results
Radius                   Area
1                        3.141592
2                        12.56637
3                        29.27433
4                        50.26548
5                        79.53981

Radius is 6
n is 5
'''

# 7.5 Hiding Data Fields
''' Direct access of a data field in an object is not a good practice for two reason:
	1. Data my be tampered with.
	2. The class becomes difficult to maintain and vulnerable to bugs.

To prevent direct modifications of data fields, don't let the client directly access data fields. This is known as data hiding. This can be done
by defining private data fields. Private data fields are defined with two leading underscores. You can also define a private method named
with two leading underscores. 

Private data fields and methods can be accessed within a class, but they cannot be accessed outside the class. To make a data field accessible for
the client, provide a get method to return its value.
'''
	# A get method has the following header:
	def getPropertyName(self):
	# If the return type is a Boolean, the get method is defined as follows by convention:
	def isPropertyNAme(self):
	#A set method has the following header:
	def setPropertyNAme(self, propertyValue):

import math

class Circle:
	# Constructs a circle object
	def __init__(self, radius = 1):
		self.__radius = radius
	def getRadius(self):
		return self.__radius
	def getPerimeter(self):
		return 2 * self.__radius * math.pi
	def getArea(self):
		return self.__radius * self.__radius * math.pi

'''The radius property cannot be directly accessed in this new Circle class. However, you can read it by using the getRadius() method:

>>>from CircleWithPirateRadius import Circle
>>>c = Circle(5)
>>>c.__radius
AttributeError: no attribute "__radius"
>>>c.getRadius()
5
>>>
'''
