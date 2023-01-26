## Nicholas Norman Oct/2022 ##
## Budget ##

#import date and time
from datetime import datetime

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

def PrintCategories(functOrList):
    #prints all fields
    categoryList = functOrList
    print("{:5} {:15} {:15} {:15}".format("", "Category", "Budgeted-Amount", "   Amount-Spent"))
    for item in range(len(categoryList)):
        print("{:4}) {:15} {:15} {:15}".format(item, categoryList[item][0], categoryList[item][1], categoryList[item][2]))
    
def SaveCategory(categoryList):
    file = open("./category.csv", "w")
    for i in range(len(categoryList)):

        for k in range(len(categoryList[i])):
            categoryList[i][k] = '"{}"'.format(categoryList[i][k])
        
        categoryList[i] = ", ".join(categoryList[i])

        if i <= 0:
            file.write(categoryList[i])
        else:
            file.write("\n{}".format(categoryList[i]))

def SaveLog(log):
    file = open("./log.txt", "a")
    currentTime = datetime.now()
    file.write(f"\n{currentTime}")
    for item in range(len(log)):
        line = log[item]
        line = ", ".join(line)
        file.write("\n" + line)
    file.close()

def SetupMode(categoryList):
    userInput = input("Would you like to enter SETUP mode?(y/n): ")
    if userInput == "y":
        keepGoing = True
        while keepGoing:
            #list all categories
            PrintCategories(categoryList)

            #ask to edit a category, or add new one
            userInput = input("Would you like to Edit?(y/n): ")
            if userInput == "y":
                #to edit,
                #change name, or price, or reset spent
                category = int(input("Select number to edit: "))

                #ask for new category, then new price, then spent
                print(categoryList[category])
                categorySub = int(input ("What would you like to edit?\n0)Name, 2)Budgeted-Amount, 3)"))
                print(categoryList[category][categorySub])
                newValue = int(input("Please enter new value: "))
                categoryList[category][categorySub] = newValue
            #save file
            else:
                keepGoing = False
    else:
        categoryList = GetCategoryList()
        
    return categoryList

def BudgetInput(categoryList, category, spent, log):
    #i = 0
    #keepGoing = True
    #while keepGoing:
        #i += 1
        #print all categories
        #PrintCategories(categoryList)

        #input: category and price
        #userInput = input("\nPlease input category number, and then the expensditure like so; <number> <expense>: ")
        #userInput = userInput.split(" ")
    for item in categoryList:
        if item[0] == category:
            categoryID = categoryList.index(item)
    spent = float(spent)
    spent = round(spent, 2)

            #add category spent + new price
    categoryList[categoryID][2] += spent
    categoryList[categoryID][2] = round(categoryList[categoryID][2], 2)

            #add to list of log files
    log.append((category, spent))

            #exit loop
        #stay = input("Press E to exit, Press S to add another expense: ")
        #if stay == "E":
            #keepGoing = False

    return categoryList, log

def SaveAndExit(categoryList, log):
    #save to category file
    SaveCategory(categoryList)

    #save to log file w/date
    SaveLog(log)

if __name__ == "__main__":
    #Start
    log = []

    #Setup mode
    categoryList = list(SetupMode(GetCategoryList()))

    #when not in setup mode
    info = [categoryList, log]
    [categoryList, log] = BudgetInput(categoryList, log)

    #end program
    SaveAndExit(info[0], info[1])

##pull spenditures from texts
##auto run program
##send emails about over under budgets
##email.sms
##scrollbar for long lists
