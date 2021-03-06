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
        calculate = investmentAmmount * (1 + annualInterestRate / 1200) ** (years * 12)
        return calculate
investCalc()

# 9.7

from tkinter import *

class drawGrid():
    def __init__(self):
        window = Tk()
        window.title("8 x 8 Grid")

        self.canvas = Canvas(window, width = 100, height = 100, bg = "white")
        self.canvas.pack()


        self.canvas.create_line(10, 20, 90, 20, tags = "line2", fill = "blue")
        self.canvas.create_line(10, 30, 90, 30, tags = "line3", fill = "blue")
        self.canvas.create_line(10, 40, 90, 40, tags = "line4", fill = "blue")
        self.canvas.create_line(10, 50, 90, 50, tags = "line5", fill = "blue")
        self.canvas.create_line(10, 60, 90, 60, tags = "line6", fill = "blue")
        self.canvas.create_line(10, 70, 90, 70, tags = "line7", fill = "blue")
        self.canvas.create_line(10, 80, 90, 80, tags = "line8", fill = "blue")


        self.canvas.create_line(20, 90, 20, 10, tags = "linea2", fill = "red")
        self.canvas.create_line(30, 90, 30, 10, tags = "linea3", fill = "red")
        self.canvas.create_line(40, 90, 40, 10, tags = "linea4", fill = "red")
        self.canvas.create_line(50, 90, 50, 10, tags = "linea5", fill = "red")
        self.canvas.create_line(60, 90, 60, 10, tags = "linea6", fill = "red") 
        self.canvas.create_line(70, 90, 70, 10, tags = "linea7", fill = "red") 
        self.canvas.create_line(80, 90, 80, 10, tags = "linea8", fill = "red")


        
drawGrid()

# 9.3


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
        self.v1.set("1")
        rbRect = Radiobutton(frame, text = "Rectangle", command = self.displayRect, variable = self.v1, value = '1')
        rbOval = Radiobutton(frame, text = "Oval", command = self.displayOval, variable = self.v1, value = '2')
        self.v2 = StringVar()
        self.v2.set("0")
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
        self.canvas.delete("rect", "oval")
        color = "white" if self.v2.get() == "0" else "red"
        if self.v1.get() == "1":
            self.canvas.create_rectangle(10, 10, 190, 90, tags = "rect", fill = color)
        else:
            self.canvas.create_oval(10, 10, 190, 90, tags = "oval", fill = color)            

            
geometricFig()


