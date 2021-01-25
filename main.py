# Hello , tkinter program for calculator

# import everything from tkinter module
from tkinter import *
import math


# globally declare the expression variable
expression = ""

# Function to update expressiom
# in the text entry box
def press(num):
    # point out the global expression variable
    global expression

    # concatenation of string
    expression = expression + str(num)

    # update the expression by using set method
    equation.set(expression)


# Function to evaluate the final expression
def equalpress():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.

    # Put that code inside the try block
    # which may generate the error
    try:

        global expression

        # eval function evaluate the expression
        # and str function convert the result
        # into string
        total = str(eval(expression))

        equation.set(total)

        # initialze the expression variable
        # by empty string
        expression = ""

        # if error is generate then handle
    # by the except block
    except:

        equation.set(" error ")
        expression = ""

    # Function to clear the contents

def getandreplace(self):

    """replace x with * and ÷ with /"""
    self.expression = self.e.get()
    self.newtext = self.expression.replace('/', '/')
    self.newtext = self.newtext.replace('x', '*')

def squareroot(self):
    """squareroot method"""
    self.getandreplace()
    try:
        # evaluate the expression using the eval function
        self.value = eval(self.newtext)
    except SyntaxError or NameError:
        self.e.delete(0, END)
        self.e.insert(0, 'Invalid Input!')
    else:
        self.sqrtval = math.sqrt(self.value)
        self.e.delete(0, END)
        self.e.insert(0, self.sqrtval)

# of text entry box
def clear():
    global expression
    expression = ""
    equation.set("")

def btnSquareRoot():
   global expression
   sqrt=math.sqrt()
   equation.set("")
   expression=""


# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()

    # set the background colour of GUI window
    gui.configure(background="yellow")

    # set the title of GUI window
    gui.title("Simple Calculator")

    # set the configuration of GUI window
    gui.geometry("580x550")

    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()

    # create the text entry box for
    # showing the expression .
    expression_field = Entry(gui,font=('arial', 20, 'bold underline'),fg = "white",bg="grey",bd = 10,textvariable=equation)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    expression_field.grid(columnspan=100, ipadx=500,ipady = 10)

    equation.set('Enter Your Expression')


    # create a Buttons and place at a particular location inside the root window .
    # when user press the button, the command or function affiliated to that button is executed .
    button1 = Button(gui, text='[ 1 ]', fg='black', bg='red', command=lambda: press(1), height=3, width=12,bd = 5,font=('arial', 12, 'bold'))
    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' [ 2 ] ', fg='black', bg='red',command=lambda: press(2), height=3, width=12,bd = 5,font=('arial', 12, 'bold'))
    button2.grid(row=2, column=1)

    button3 = Button(gui, text='[ 3 ]', fg='black', bg='red',command=lambda: press(3), height=3, width=12,bd = 5,font=('arial', 12, 'bold'))
    button3.grid(row=2, column=2)

    button4 = Button(gui, text='[ 4 ]', fg='black', bg='red',command=lambda: press(4), height=3, width=12,bd = 5,font=('arial', 12, 'bold'))
    button4.grid(row=3, column=0)

    button5 = Button(gui, text='[ 5 ]', fg='black', bg='red',command=lambda: press(5), height=3, width=12,bd = 5,font=('arial', 12, 'bold'))
    button5.grid(row=3, column=1)

    button6 = Button(gui, text='[ 6 ]', fg='black', bg='red',command=lambda: press(6), height=3, width=12,bd = 5,font=('arial', 12, 'bold'))
    button6.grid(row=3, column=2)

    button7 = Button(gui, text='[ 7 ]', fg='black', bg='red',command=lambda: press(7), height=3, width=12,bd = 5,font=('arial', 12, 'bold'))
    button7.grid(row=4, column=0)

    button8 = Button(gui, text='[ 8 ]', fg='black', bg='red',command=lambda: press(8), height=3, width=12,bd = 5,font=('arial', 12, 'bold'))
    button8.grid(row=4, column=1)

    button9 = Button(gui, text='[ 9 ]', fg='black', bg='red',command=lambda: press(9), height=3, width=12,bd = 5,font=('arial', 12, 'bold'))
    button9.grid(row=4, column=2)

    button0 = Button(gui, text='[ 0 ]', fg='black', bg='red',command=lambda: press(0), height=3, width=12,bd = 5,font=('arial', 12, 'bold'))
    button0.grid(row=5, column=0)

    plus = Button(gui, text='[ + ]', fg='black', bg='purple',command=lambda: press("+"), height=3, width=12,bd = 5,font=('arial', 12, 'bold'))
    plus.grid(row=2, column=3)

    minus = Button(gui, text='[ - ]', fg='black', bg='purple',command=lambda: press("-"), height=3, width=12,bd = 5,font=('arial', 12, 'bold'))
    minus.grid(row=3, column=3)

    multiply = Button(gui, text='[ x ]', fg='black', bg='purple',command=lambda: press("x"), height=3, width=12,bd = 5,font=('arial', 12, 'bold'))
    multiply.grid(row=4, column=3)

    divide = Button(gui, text='[ / ]', fg='black', bg='purple',command=lambda: press("/"), height=3, width=12,bd = 5,font=('arial', 12, 'bold'))
    divide.grid(row=5, column=1)

    percent = Button(gui, text='[ % ]', fg='black', bg='purple', command=lambda: press("%"), height=3, width=12,bd = 5,font=('arial', 12, 'bold'))
    percent.grid(row=5, column=2)

    leftbrace = Button(gui, text='[ ( ]', fg='black', bg='green', command=lambda: press("("), height=3, width=12, bd=5,font=('arial', 12, 'bold'))
    leftbrace.grid(row=6, column=0)

    rightbrace = Button(gui, text='[ ) ]', fg='black', bg='green', command=lambda: press(")"), height=3, width=12, bd=5,font=('arial', 12, 'bold'))
    rightbrace.grid(row=6, column=1)

    pi = Button(gui, text='[ π ]', fg='black', bg='green', command=lambda:press("3.1415"), height=3, width=12, bd=5,font=('arial', 12, 'bold'))
    pi.grid(row=6, column=2)

    btnSquareRoot = Button(gui, text='[ √ ]', fg='black', bg='green', command=lambda:press("√"), height=3, width=12, bd=5,font=('arial', 12, 'bold'))
    btnSquareRoot.grid(row=6, column=3)

    equal = Button(gui, text='[ = ]', fg='black', bg='brown',command=equalpress, height=3, width=24,bd = 5,font=('arial', 12, 'bold'))
    equal.grid(row=7, column=0,columnspan = 2)

    clear = Button(gui, text='[ Clear ]', fg='black', bg='brown',command=clear, height=3, width=24,bd = 5,font=('arial', 12, 'bold'))
    clear.grid(row=7, column=2,columnspan = 2)

    Decimal = Button(gui, text='[ . ]', fg='black', bg='green',command=lambda: press('.'), height=3, width=12,bd = 5,font=('arial', 12, 'bold'))
    Decimal.grid(row=5, column=3)

    # start the GUI
    gui.mainloop()