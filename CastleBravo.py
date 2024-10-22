print("\n ****************************************\n")

print("Gasoline Branch")

import random
from time import sleep

def gasLevelGaugue():
    gasLevelList = ["Empty","Low","Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    return random.choice(gasLevelList)

def gasStations():
    gasStationsList = ["BP", "Shell", "Meijer", "Sams club","Marathon", "Mobile","Speedway","Circle K"]
    return random.choice(gasStationsList)

def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1,25),1)
    milesToGasSTationQuarterTank = round(random.uniform(25.1,50),1)
    gasLevelIndicator = gasLevelGaugue()
    if gasLevelIndicator == "Empty":
        print("\n***WARNING - YOU ARE ON EMPTY***\n")
        sleep(2)
        print("Calling Triple AAA")
    elif gasLevelIndicator == "Low":
        print("Your Gas Tank Is Extremely Low, Checking GPS for The Closest Gas Station")
        sleep(2)
        print("The Closest Gas Station is",gasStations(),"Which is",milesToGasStationLow,"Miles Away")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your Gas Tank Is a Quarter of a Tank, Checking GPS for The Closest Gas Station")
        sleep(2)
        print("The Closest Gas Station is", gasStations(), "Which is", milesToGasSTationQuarterTank, "Miles Away")
    elif gasLevelIndicator == "Half Tank":
        print("Your Gas Tank is Half-way Empty, which leaves plenty to get to your Destination.")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your Gas Tank is 3/4 full, which leaves plenty to get to your Destination.")
    else:
        print("Your Gas Tank is Full!")



gasLevelAlert()