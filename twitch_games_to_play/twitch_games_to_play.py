## Twitch games to play ##
## Take list, ask for priority, then randomly sort with different priorities ##


import random

games = []
gamesSorted = []

def importGames():
    #import file
    file = open(r"./twitchgamestoplay.txt", "r")
    for line in file:
        #remove \n after each line
        line = line.replace("\n", "")
        line = line.strip()
        
        #add each item to list with default ranking
        games.append([line, 5])

def askForPriority():
    #Go through each game
    print("Rate each game from 1 to 5, 1 being most want to play")
    for i in range(len(games)):
        #Ask for priority
        priority = input("{}: ".format(games[i][0]))
        #save to array
        games[i] = [games[i][0], priority]

def sortByPrior(rank):
    gamesByRank = []
    gamesByRand = []
    
    #sort each by priority  
    for i in range(len(games)):
        if games[i][1] == rank:
            gamesByRank.append([games[i]])

    #pick random
    for i in range(len(gamesByRank)):
        rand = random.randint(0, len(gamesByRank))
        var = gamesByRank.pop(gamesByRank[rand])
        gamesByRand.append(var)

    #save to sorted list
    for i in range(len(gamesByRand)):
        gamesSorted.append(gamesByRand[i])
    

#main
if __name__ == "__main__":
    importGames()
    askForPriority()
    for i in range(1,5):
        sortByPrior(i)
                               
    print(gamesSorted)
