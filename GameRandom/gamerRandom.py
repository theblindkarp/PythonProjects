import random as rn

gamesList = []

#read all games from txt file
file = open("gamesList.txt", "r")

#set each to list
for line in file:
    gamesList.append(line)
    
#find random number from index of list
gameID = rn.randint(0, len(gamesList) - 1)

#print
print("The game I decided you shall play is:")
print(gamesList[gameID])

dummy = input("This is a dummy: ")
