from tkinter import *
import budget as bgt

root = Tk()
root.title("Budget")

def LabelUpdate(categoryList):
    categoryList = categoryList
    info = ["", "", ""]
    titles = ["{:25}\n".format("Category"), "{:>25}\n".format("Budgeted"), "{:>25}\n".format("Spent")]
    info0 = Label(root, text = "")
    info1 = Label(root, text = "")
    info2 = Label(root, text = "")
    infoLabel = [info0, info1, info2]
    for k in range(len(info)):
        for i in range(len(categoryList)):
            if k == 0:
                info[k] = info[k] + "{:25}\n".format(categoryList[i][k])
            if k > 0:
                info[k] = info[k] + "${:.>25}\n".format(categoryList[i][k])

    for i in range(len(infoLabel)):
        if i == 0:
            infoLabel[i] = Label(root, text = titles[i] + info[i], justify = "left")
        if i > 0:
            infoLabel[i] = Label(root, text = titles[i] + info[i], justify = "right")

    for i in range(0, len(categoryList) - 1):
        infoLabel[i].grid(row = 0, column = i)

    global justCategories
    for i in range(len(categoryList)):
        justCategories.append(categoryList[i][0])
    print("LabelUpdated")

def SubmitButton():
    global categoryList
    global log
    ErrorMessage("{:100}".format(""))
    category = categoryDropVar.get()
    spent = costBox.get()
    try:
        float(spent)
        if category == "Category":
            1 + "7"
        i = 1
    except:
        ErrorMessage("Incorrect Input Value(s)")
        i = 0
        
    if i == 1:
        (categoryList, log) = bgt.BudgetInput(categoryList, category, spent, log)
        LabelUpdate(categoryList)
        categoryBox.delete(0, END)
        costBox.delete(0, END)

def ErrorMessage(error):
    global errorMessages
    errorMessages = error
    errors = Label(root, text = errorMessages)
    errors.grid(row = 3, column = 0, columnspan = 3)

def Exit():
    global categoryList
    global log
    bgt.SaveAndExit(categoryList, log)
    root.destroy()

#Variables and Start
justCategories = [" Category"]
log = []
errorMessages = ""
categoryList = bgt.GetCategoryList()
LabelUpdate(bgt.GetCategoryList())

#Buttons
submitButton = Button(root, text = "{:>}".format("submit"), command = SubmitButton, width = 20)

#Dropdown box
categoryDropVar = StringVar()
categoryDropVar.set("Category")
categoryDrop = OptionMenu(root, categoryDropVar, *justCategories)

#Button
exitSave = Button(root, text = "Save & Exit", width = 55)

#Entrys
costBox = Entry(root)
categoryBox = Entry(root)
costBox.insert(0, "Spent")
categoryBox.insert(0, "Category")

#Labels

#Display
categoryDrop.grid(row = 1, column = 0, padx = 1)
costBox.grid(row = 1, column = 1)
submitButton.grid(row = 1, column = 2)
exitSave.grid(row = 2, column = 0, columnspan = 3)

#End loop
root.mainloop()
