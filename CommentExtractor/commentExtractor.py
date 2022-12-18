## Nicholas Norman Oct/2022 ##
## Comment Extractor ##
cmtCht = input("What is the comment character?: ")
comments = []

file = open(r"./input.txt", "r")

for line in file:
    if cmtCht in line:
        comments.append(line)
file.close()

print(comments)

file = open(r"./output.txt", "w")

for i in range (len(comments)):
    file.write(comments[i])

file.close()

dummy = input(""" Output was saved to ./output.txt
press ENTER to close program """)
