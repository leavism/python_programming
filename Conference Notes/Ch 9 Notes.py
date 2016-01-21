# 9.2 Getting started with Tkinter
'''
The tkinter module contains the classes for creating GUIs. The Tk class creates a window for holding GUI widgets.
'''

from tkinter import *

window = Tk() # Create a window
label = Label(window, text = "Welcome to Python") # Create a label
button = Button(window, text = "Click Me") # Create a button
label.pack() # Place label in the window
button.pack() # Place a button in the window

window.mainloop() # Create an event loop

# 9.3 Processing Events
'''
When the user clicks a button, your program should process this event. You enable this action by
defining a processing function and binding the function to the button
'''

from tkinter import *

def processOK(): # These are called callback functions or handlers
    print("Ok button is clicked")

def processCancel(): # These are called callback functions or handlers
    print("Cancel button is clicked")

window = Tk()
btOK = Button(window, text = "OK", fg = "red", command = processOK)
btCancel = Button(window, text = "Cancel", bg = "yellow", command = processCancel)

btOK.pack()
btCancel.pack()

window.mainloop()

'''
You can also write this program by placingall the functions in one class.
'''

from tkinter import *

class ProcessButtonEvent:
    def __init__(self):
        window = Tk()
        btOK = Button(window, text = "OK", fg = "red", command = self.processOK)
        btCancel = Button(window, text = "Cancel", bg = "yellow", command = processCancel)

        btOK.pack()
        btCancel.pack()

        window.mainloop()

    def processOK(self):
        print("Ok butotn is clicked")
    def processCancel(self):
        print("Cancel button is clicked")

ProcessButtonEvent()

# 9.4 The Widget Classes
'''
To specify a color, use either a color name or explicitly specify the RGB color components by using a string #RRGGBB.

By default, the text in a label or a button is centered. You can change its alignment by using the justify option with the named
constants LEFT, CENTER, or RIGHT.

You can specify a particular style of mouse cursor by using the cursor option with string values such as ARROW, CIRCLE, CROSS, PLUS.

When you construct a widget, you can specify its properties such as fg, bf, font, cursor, text, and command in the constructor.
'''

'''
The following creates a button and its text property is changed to Hide, bg property to red, and fg to #AB84F9.

btShowOrHide = Button(window, text = "Show", bg = "white")
btShowOrHide["text"] = "Hide"
btShowOrHide["bg"] = "red"
btShowOrHide["fg"] = "#AB84F9"
btShowOrHide["cursor"] = "plus"
btShowOrHide["justify"] = LEFT
'''
from tkinter import *

class ChangeLabelDemo:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Change label Demo") # Set a title

        #Add a label to frame1
        frame1 = Frame(window) # Creates and add a frame to window
        frame1.pack()
        self.lbl = Label(frame1, text = "Programming is fun")
        self.lbl.pack()
        # Add a label, entry, button, two radio buttons to frame2
        frame2 = Frame(window) # Create and add a frame to window
        frame2.pack()
        label = Label(frame2, text = "Enter text: ")
        self.msg = StringVar()
        entry = Entry(frame2, textvariable = self.msg)
        btChangeText = Button(frame2, text = "Change Text", command = self.processButton)
        self.v1 = StringVar()
        rbRed = Radiobutton(frame2, text = "Red", bg = "Red", variable = self.v1, value = 'R', command = self.processRadiobutton)
        rbYellow = Radiobutton(frame2, text = "Yellow", bg = "Yellow", variable = self.v1, value = 'Y', command = self.processRadiobutton)

        label.grid(row = 1, column = 1)
        entry.grid(row = 1, column = 2)
        btChangeText.grid(row = 1, column = 3)
        rbRed.grid(row = 1, column = 4)
        rbYellow.grid(row = 1, column = 5)

        window.mainloop()
    def processRadiobutton(self):
        if self.v1.get() == 'R':
            self.lbl["fg"] = "Red"
        elif self.v1.get() == 'Y':
            self.lbl["fg"] = "Yellow"

    def processButton(self):
        self.lbl["text"] = self.msg.get()

ChangeLabelDemo()


