#Trillion Test
#Nicholas Norman Nov. 2022
import datetime

def main():
    numToGetTo = 1_000_000
    print(f"numToGetTo is default {numToGetTo:,}")
    
    step = input("Step: ")
    step = int(step)

    start = datetime.datetime.now()

    i = 0
    keepGoing = True
    while keepGoing:
        i += 1

        if step > 0:
            if i % step == 0:
                print(f"{i:,}")

        if i >= numToGetTo:
            keepGoing = False
            end = datetime.datetime.now()

            secondsTotal = (end - start).total_seconds()
            secondsTotal = round(secondsTotal, 3)
            
            print(f"Reached {i:,} {secondsTotal:,} seconds")

    output = input("Press 1 to Exit: ")
    return output

if __name__ == "__main__":
    x = 0
    while x != 1:
        x = main()

