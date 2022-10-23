## Nicholas Norman 10/2022 ##

#Variables
    #create List of items on menu and prices
menu = ["Snickers", "Poptart", "20 lbs of Gummy Worms"]
menuPrices = [3.99, 1.49, 89.99]
    #create denomination list
denominations = [100, 50, 20, 10, 5, 1, 0.5, 0.25, 0.1, 0.05, 0.01]
denoNames = ["Hundreds", "Fifties", "Twneties", "Tens", "Fives", "Ones", "Half Dollars", "Quarters", "Dimes", "Nickels", "Pennies"]
    #create amount of change list
billCount = [0,0,0,0,0,0,0,0,0,0,0]
    #Input variables
moneyTaken = 0
userInput = 0
change = 0

def ItemSelection():
    #asks for selection
        #force int
    keepGoing = True
    while (keepGoing):
        global userInput
        userInput = int((input("Please select item: ")))
        if userInput in range(0,len(menu)):
            price = menuPrices[userInput]
            keepGoing = False
        else:
            print("invalid input.")

    return price

def ChangeCalc(d):
    global change
    billCount[d] = int(change // denominations[d])
    change = change % denominations[d]

#print items on list
print("Welcome to Python's very own digital vending machine!")
for i in range(len(menu)): #takes into account no first item
    print("{}: {}: ${}".format(i, menu[i], menuPrices[i]))

#ask user for item selection
price = ItemSelection()
print(price)

#calculate change

#ask user for credit or cash
payMethod = int(input("Credit or Cash? (1 for Credit, 2 for Cash): "))
    #if credit, approval screen
if payMethod == 1:
    print("credit approved. Thank you.")
    #if cash, take input
if payMethod == 2:
    moneyGiven = input("How much would you like to insert?: ")
    price = float(price)
    moneyGiven = float(moneyGiven)
    change = moneyGiven - price

        #start Divide and save amount to 'amount of change list'
    for i in range(len(denominations)):
        ChangeCalc(i)

    #print transaction complete
    print("Transaction Complete. Your change is {}".format(round(moneyGiven - price, 2)))
    #print change and amount of bills given
    for j in range (len(denominations)):
        print("You will recieve {} {}".format(billCount[j], denoNames[j]))

#print item to be given to user
print("Thanks for choosing PythonVendingCo.")
print("*Drops Digital {}*".format(menu[userInput]))

dummy = input("press ENTER to close program")



