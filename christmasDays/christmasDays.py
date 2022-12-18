## Twelve Days of Christmas Calc ##
## Nicholas Norman Oct/2022 ##

lineNumber = 0
itemList = []
numSuf = ["st", "nd", "rd", "th"]

file = open(r"./itemList.csv", "r")
for line in file:
    lineNumber += 1
    line = line.strip()
    line = line.replace('"', '')
    currentLine = line.split(",")
    itemList.insert(lineNumber, currentLine)

file.close()

"""
for i in range(len(itemList)):
    #take second number in i
    iNum = (i + 1) / 10
    iNum %= 1
    iNum = round(iNum, 2)
    iNum *= 10
    iNum = int(iNum)

    if i + 1 in (11, 12, 13):
        suffix = numSuf[3]
    elif iNum in (1, 2, 3):
        suffix = numSuf[iNum - 1]
    else:
        suffix = numSuf[3]
    
    print("on the {:2}{} day of christmas, my true love gave to me,{} {}".format(i + 1, suffix, itemList[i][1], itemList[i][0]))
"""

userInput = input("What day of christmas is it (1-{})?: ".format(len(itemList)))
userInput = int(userInput)
for i in range(0, userInput):
    itemSum = ((userInput - (int(itemList[i][1]) - 1)) * int(itemList[i][1])) 
    print("you will have {:3} {}".format(itemSum, itemList[i][0]))

dummy = input("press Enter to continue")

##goal
#one the X day of christmas you will get X {item}
#input (number), return how many of each item
    

