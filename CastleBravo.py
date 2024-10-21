print("\n ****************************************\n")

print("Gasoline Branch")

import random
from time import sleep

def gasLevelGaugue():
    gasLevelList = ["Empty","Low","Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    return random.choice(gasLevelList)

def gasStations():
    gasStationsList = ["vp", "Shell", "Meijer", "Sams club","Marathon", "Mobile","Speedway","Circle K"]
    return random.choice(gasStationsList)

print(gasLevelGaugue())
print(gasStations())
#def gasLevelAlert