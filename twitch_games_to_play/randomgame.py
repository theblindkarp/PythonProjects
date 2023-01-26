import random

games = []

#import file
file = open(r"./twitchgamestoplay.txt", "r")
for line in file:
    #remove \n after each line
    line = line.replace("\n", "")
    line = line.strip()

    games.append(line)

var = random.randint(0, len(games))
print("You should play: {}".format(games[var]))
