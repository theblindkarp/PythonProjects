import random

keepGoing = True
while keepGoing: 
    percent = random.randint(1,100);
    nameNum = int(input("How many people are in the relationship?: "));
    nameList = []
    if nameNum == 69:
        nameNum = int(input("How many people are in the relationship?: "))
        sixNineAccess = True;
    for i in range(nameNum):
        nameTemp = input(f"What is person {i + 1}'s name: ")
        nameList.append(nameTemp)
    lastName = nameList[len(nameList) - 1]
    nameList.remove(nameList[len(nameList) - 1])
    nameListJoin = ", ".join(nameList)

    if sixNineAccess == False:
        if nameNum <= 1:
            percent = random.randint(90,100)
            print("{} have a {}% chance of love".format(lastName, percent))
        else:
            print("{} and {} have a {}% chance of love".format(nameListJoin, lastName, percent))
            print()
    else:
        percent = int(input("enter random number: "))
        percent += 50
        print("{} and {} have a {}% chance of love".format(nameListJoin, lastName, percent))

    dummy = input("press 7 to exit: ")
    if dummy == "7":
        keepGoing = False
    
