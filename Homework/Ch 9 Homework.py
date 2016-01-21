# 9.2
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
        calculate = investmentAmmount * (1 + annualInterestRate / 12) ** (years * 12)
        return calculate
investCalc()
# 9.7

# 9.3
class geometricFig:
    def __init__(self):
        window = Tk()
        window.title("Geometric Figures") 

        self.canvas = Canvas(window, width = 200, height = 100, bg = "white")
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()
        rbRect = Radiobutton(frame, text = "Rectangle")
        rbOval = Radiobutton(frame, text = "Oval")
        window.mainloop()
        
geometricFig()
