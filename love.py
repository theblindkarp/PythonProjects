import random

keepGoing = True
while keepGoing:
    percent = random.randint(1,100)
    nameNum = int(input("How many people are in the relationship?: "))
    nameList = []
    for i in range(nameNum):
        nameTemp = input(f"What is person {i + 1}'s name: ")
        nameList.append(nameTemp)
    lastName = nameList[len(nameList) - 1]
    nameList.remove(nameList[len(nameList) - 1])
    nameListJoin = ", ".join(nameList)
    if nameNum <= 1:
        print("{} have a {}% chance of love".format(nameListJoin, percent))
    else:
        print("{} and {} have a {}% chance of love".format(nameListJoin, lastName, percent))
    dummy = input("press 7 to exit: ")
    if dummy == "7":
        keepGoing = False
