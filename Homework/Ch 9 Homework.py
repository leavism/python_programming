# 9.2
'''
from tkinter import *

class investCalc:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Investment-Value Calculator")

        Label(window, text = "Investment amount").grid(row = 1, column = 1, sticky = W)
        Label(window, text = "Years").grid(row = 2, column = 1, sticky = W)
        Label(window, text= "Annual Interst Rate").grid(row = 3, column = 1, sticky = W)
        Label(window, text = "Future Value").grid(row =4, column = 1, sticky = W)
        
        self.investmentAmmountVar = StringVar()
        Entry(window, textvariable = self.investmentAmmountVar, justify = RIGHT).grid(row = 1, column = 2)
        self.yearsVar = StringVar()
        Entry(window, textvariable = self.yearsVar, justify = RIGHT).grid(row =2, column = 2)
        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable = self.annualInterestRateVar, justify = RIGHT).grid(row = 3, column = 2)

        self.futureValueVar = StringVar()
        lblFutureValue = Label(window, textvariable = self.futureValueVar).grid(row = 4, column = 2, sticky = E)

        btCalculate = Button(window, text = "Calculate", command = self.calculate).grid(row = 5, column = 2, sticky = E)

        window.mainloop()
    def calculate(self):
        calculate = self.getCalculate(
            float(self.investmentAmmountVar.get()),
            int(self.yearsVar.get()),
            float(self.annualInterestRateVar.get()))
        self.futureValueVar.set(format(calculate, "10.2f"))
                                
    def getCalculate(self, investmentAmmount, years, annualInterestRate):
        calculate = investmentAmmount * (1 + annualInterestRate / 1200) ** (years * 12)
        return calculate
investCalc()
'''
# 9.7

from tkinter import *

class drawGrid():
    def __init__(self):
        window = Tk()
        window.title("8 x 8 Grid")

        self.canvas = Canvas(window, width = 200, height = 200, bg = "white")
        self.canvas.pack()
        
        self.canvas.create_line(10, 10, 190, 10, tags = "line1", fill = "red")
        window.mainloop()

        
drawGrid()

# 9.3

'''
from tkinter import *

class geometricFig:
    def __init__(self):
        window = Tk()
        window.title("Geometric Figures") 

        self.canvas = Canvas(window, width = 200, height = 100, bg = "white")
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()
        self.v1 = StringVar()
        rbRect = Radiobutton(frame, text = "Rectangle", command = self.displayRect, variable = self.v1, value = '1')
        rbOval = Radiobutton(frame, text = "Oval", command = self.displayOval, variable = self.v1, value = '2')
        self.v2 = StringVar()
        cbtFill = Checkbutton(frame, text = "Fill", command = self.processFill, variable = self.v2)

        rbRect.grid(row = 1, column = 1)
        rbOval.grid(row = 1, column = 2)
        cbtFill.grid(row = 1, column = 3)
        
        window.mainloop()
    
    def displayRect(self):
        self.canvas.delete("rect", "oval")
        self.canvas.create_rectangle(10, 10, 190, 90, tags = "rect")
    def displayOval(self):
        self.canvas.delete("rect", "oval")
        self.canvas.create_oval(10, 10, 190, 90, tags = "oval")
    def processFill(self):
        if self.v1.get() == '1':
            self.canvas.delete("rect", "oval")
            self.canvas.create_rectangle(10, 10, 190, 90, tags = "rect", fill = "red")
        elif self.v1.get() == '2':
            self.canvas.delete("rect", "oval")
            self.canvas.create_oval(10, 10, 190, 90, tags = "oval", fill = "red")
        else:
            self.canvas.delete("rect", "oval")
            
geometricFig()

'''
