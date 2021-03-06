class rectangle:
	def __init__(self, width = 1, height = 2):
		self.__width = width
		self.__height = height
	def getWidth(self):
		return self.__width
	def setWidth(self):
		self.__width = width
	def getHeight(self):
		return self.__height
	def setHeight(self):
		self.__height = height
	def getArea(self):
		return self.__width * self.__height
	def getPerimeter(self):
		return self.__width * 2 + self.__height * 2

''' UML Diagram
rectangle
-----------
-width: float
-height: float
-----------
rectangle(width = 1, height =2)
getWidth(): float
setWidth(width = 1): none
getHeight(): float
setHeight(height = 2): none
getArea(): float
getPerimeter(): float
'''