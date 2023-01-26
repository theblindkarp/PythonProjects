## Nicholas P Norman ##
## Dec 2022 ##

#List of sample values
tundaList = [1, "2", 45, "Seven"]

def isInt(tundaList, index):
    #checks if the value in the list can be converted to int
    try:
        #try to cast the value as an int
        int(tundaList[index])
    except:
        #if this provides an error, then print it cannot be converted
        print("This index is not an integer")
    else:
        #if there is no error, provide the int in question
        print("It is an int: {}".format(tundaList[index]))

#ask for index of list to check
index = int(input("please provide an integer: "))

#call function isInt
isInt(tundaList, index)
