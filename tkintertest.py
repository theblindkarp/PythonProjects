from tkinter import *

#window setup
root = Tk()
root.title("Width and Length")

#function for button
def ButtonPress():
    width = int(entry.get())
    length = int(entry2.get())
    
    row = "_" * width
    column = ("|" + " " * (width) + "|\n") * length
    rectangle = f"{row}\n{column}{row}"

    top = Toplevel()
    top.title("Rectangle")

    myLabel = Label(top, text = rectangle)
    myLabel.grid(row = 10, column = 0, columnspan = 2)


#entry (input field) widget
entry = Entry(root, width = 25)
entry2 = Entry(root, width = 25)
entry.insert(0, "Enter Width")
entry2.insert(0, "Enter Length")

#label widget for root
myLabel = Label(root, text = "|_|")
myButton3 = Button(root, text = "Make Rectangle", command = ButtonPress)

#display on screen
myButton3.grid(row = 2, column = 0, columnspan = 2)
entry.grid(row = 1, column = 0)
entry2.grid(row = 1, column = 1)

#loop until program ends
root.mainloop()


