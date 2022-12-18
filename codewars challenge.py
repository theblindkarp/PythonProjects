def subtract_sum(n):
    #take n
    #make sure n is in range from 10 to 10,000
    if n >= 10:
        if n <= 10_000:
            keepGoing = True
    else:
        keepGoing = False
        output = "No Fruit"
    
    #loop until get a fruit
    while keepGoing:
    #turn all digits into a list of ints
        #convert n to str
        n = str(n)
        #for every char in str, add to list
        nList = []
        for char in n:
            nList.append(char)
        #convert each char on list to int
        for i in range(len(nList)):
            nList[i] = int(nList[i])
    #add all items in the list
        for int in nList:
            sum += int
    #subtract the sum from n
        fruitID = n - sum
    #use as index in list
        output = fruitID
        keepGoing = False
    return output #fruit name like "apple"
