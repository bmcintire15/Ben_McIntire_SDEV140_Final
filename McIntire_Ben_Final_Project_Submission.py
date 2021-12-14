#  This GUI Program is based off a fake Pizzeria known as Momma Mia's Pizzeria. It will include the sandwich
#  customization area of their application.
#
#     Variables:
#   addPremade - This defines the pre-made sandwiches on the menu
#   submitOrder - This variable triggers the total to be calculated and for the total to pop up in another window.
#   exitProgram - This variable sets up the kill-switch to the program so that a user may exit the program

# The first step to this program was to import the TKinters
# First is importing Tkinter as tk so I can abbreviate my TKinters into tk
#  Next is to import all as * so I can use TKinter more broadly
#   Lastly is to import the messagebox as a popup window which will be used later.
import tkinter as tk
from tkinter import *
from tkinter import messagebox

# Starting with adding my variables, I set up the defining requirements for Premades, Submission, and an exit button
totalCost = 0
def addPremade(cost):
    global totalCost
    totalCost += cost

#  This def allows generation of the box which displays the total cost of the sandwiches
def submitOrder(totalCost):
    tk.messagebox.showinfo(message= "Your total comes to: $" + str(totalCost))

def exitProgram():
    window.destroy()


# The following information includes my tkinter options for the sandwiches you can purchase from the restaurant, calling
# from the previously defined statements
window = tk.Tk()
title = tk.Label(text="Welcome to Momma Mia's! What would you like to order?")
option1 = tk.Button(text="Chicken N' BBQ", command=lambda :addPremade(9.99))
option2 = tk.Button(text="Pizza Sandwich", command=lambda :addPremade(11.99))
option3 = tk.Button(text="Chicken Parm", command=lambda :addPremade(7.99))
submitButton = tk.Button(text="Click Here to submit your order", command=lambda :submitOrder(totalCost))
exitButton = tk.Button(text="Exit", command=exitProgram)



# This section is where the program is set up visually. This is what the .pack does
#   Each .pack visualizes each element to be displayed on screen
#   Starting with the title, and ending with the exit button.

title.pack()
option1.pack()
option2.pack()
option3.pack()
submitButton.pack()
exitButton.pack()

tk.mainloop()