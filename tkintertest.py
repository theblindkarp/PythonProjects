from tkinter import *

#window setup
root = Tk()
root.title("Test Application")
root.iconbitmap(r"./lols.ico")



#function for button
def ButtonPress():
    print("button pressed")
    myLabel = Label(root, text = entry.get())
    myLabel.grid(row = 0, column = 0)

#entry (input field) widget
entry = Entry(root, width = 50, borderwidth = 12)
entry.insert(0, "Enter Your Name")

#label widget for root
myLabel = Label(root, text = "Name")
#gridLabel = Label(root, text = "This is useing the grid system")
#testLabel = Label(root, text = "What row is this?")

#button creation
#disabled button
#myButton = Button(root, text = "click me", state = DISABLED)
#myButton2 = Button(root, text = "I padded this!", padx = 12, pady = 7, command = ButtonPress) #Keep in mind no () on funt
myButton3 = Button(root, text = "Enter Name", command = ButtonPress)
button_quit = Button(root, text = "Exit", command = root.destroy)

#display on screen
#myLabel.pack()
myLabel.grid(row = 0, column = 0)
#gridLabel.grid(row = 2, column = 1)
#testLabel.grid(row = 0, column = 2)
#myButton.grid(row = 0, column = 5)
#myButton2.grid(row = 7, column = 7)
myButton3.grid(row = 1, column = 0)
entry.grid(row = 2, column = 0)
button_quit.grid(row = 3, column = 0)


top = Toplevel()
lbl = Label(top, text = "Hello World")
lbl.pack()

#loop until program ends
root.mainloop()


