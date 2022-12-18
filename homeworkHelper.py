##Homework Helper##
##Nicholas Norman Oct/2022##

from tkinter import *

root = Tk()
root.title = "Homework Helper"

def hwLabel():
    i = 7
    hwLabel = '\n'.join(hwList)
    return hwLabel

def submit():
    hwList.append(hwEntry.get())
    hwEntry.delete(0, END)
    hw = Label(root, text = hwLabel(), justify = "left")
    hw.grid(row = 0, column = 0, columnspan = 2)

#Variables
hwList = []

#Labels
hw = Label(root, text = hwList)
hwEntry = Entry(root)
submit = Button(root, text = "submit", command = submit)

#Display
hw.grid(row = 0, column = 0, columnspan = 2)
hwEntry.grid(row = 1, column = 0)
submit.grid(row = 1, column = 1, padx = 20)

root.mainloop()
