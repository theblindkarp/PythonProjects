from tkinter import *

root = Tk()
root.title("Budget")

#gets list
def GetCategoryList():
    #converts category csv to list
    lineNumber = 0
    categoryList = []
    file = open("./category.csv", "r")
    for line in file:
        lineNumber += 1
        line = line.strip()
        line = line.replace('"', '')
        currentLine = line.split(",")
        #assign each line to list
        currentLine[1] = int(currentLine[1])
        currentLine[2] = int(currentLine[2])
        categoryList.insert(lineNumber, currentLine)
    file.close()
    
    return categoryList

#Variables and lists
categoryList = GetCategoryList()
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
            info[k] = info[k] + "{:.>25}\n".format(categoryList[i][k])

#Buttons
submitButton = Button(root, text = "{:>}".format("submit"), width = 20)
exitSave = Button(root, text = "Save & Exit", width = 55)

#Entrys
costBox = Entry(root)
categoryBox = Entry(root)
costBox.insert(0, "Spent")
categoryBox.insert(0, "Category")

#Labels
for i in range(len(infoLabel)):
    if i == 0:
        infoLabel[i] = Label(root, text = titles[i] + info[i], justify = "left")
    if i > 0:
        infoLabel[i] = Label(root, text = titles[i] + info[i], justify = "right")

#Display
for i in range(len(categoryList)):
    infoLabel[i].grid(row = 0, column = i)
categoryBox.grid(row = 1, column = 0, padx = 1)
costBox.grid(row = 1, column = 1)
submitButton.grid(row = 1, column = 2)
exitSave.grid(row = 2, column = 0, columnspan = 3)

#End loop
root.mainloop()
