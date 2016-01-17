class account:
	def __init__(self, id = 0, balance = 100, annualInterestRate = 0):
		self.__id = id
		self.__balance = balance
		self.__annualInterestRate = annualInterestRate
	def setId(self, id):
		self.__id = id
	def setBalance(self, balance):
		self.__balance = balance
	def setAnnualInterestRate(self, annualInterestRate):
		self.__annualInterestRate = annualInterestRate / 1000
	def getMonthlyInterestRate(self):
		return self.__annualInterestRate / 12
	def getMonthlyInterest(self):
		monthlyInterestRate = self.__annualInterestRate / 12
		return self.__balance * monthlyInterestRate
	def withdraw(self, amount):
		if self.__balance > 1:
			self.__balance -= amount
	def deposit(self, amount):
		self.__balance += amount
	def getId(self):
		return self.__id
	def getBalance(self):
		return self.__balance
	def getAnnualInterestRate(self):
		return self.__annualInterestRate