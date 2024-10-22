import random
from time import sleep

# Defining gas levels and gas stations globally so they don't need to be redefined every time
gasLevels = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
gasStationsList = ["BP", "Shell", "Meijer", "Sams club", "Marathon", "Mobile", "Speedway", "Circle K"]

# Function to randomly select a gas level
def gasLevelGauge():
    return random.choice(gasLevels)

# Function to randomly select a gas station
def gasStations():
    return random.choice(gasStationsList)

# Function to check the gas level and display alerts or instructions
def gasLevelAlert():
    gasLevelIndicator = gasLevelGauge()
    milesToStation = {
        "Low": round(random.uniform(1, 25), 1),
        "Quarter Tank": round(random.uniform(25.1, 50), 1)
    }

    # Dictionary to map gas levels to messages and actions
    gasActions = {
        "Empty": lambda: print("\n***WARNING - YOU ARE ON EMPTY***\nCalling Triple AAA"),
        "Low": lambda: print(f"Your Gas Tank Is Extremely Low, Checking GPS for The Closest Gas Station\n"
                             f"The Closest Gas Station is {gasStations()} Which is {milesToStation['Low']} Miles Away"),
        "Quarter Tank": lambda: print(f"Your Gas Tank Is a Quarter of a Tank, Checking GPS for The Closest Gas Station\n"
                                      f"The Closest Gas Station is {gasStations()} Which is {milesToStation['Quarter Tank']} Miles Away"),
        "Half Tank": lambda: print("Your Gas Tank is Half-way Empty, which leaves plenty to get to your destination."),
        "Three Quarter Tank": lambda: print("Your Gas Tank is 3/4 full, which leaves plenty to get to your destination."),
        "Full Tank": lambda: print("Your Gas Tank is Full!")
    }

    # Execute the corresponding action based on the gas level
    print("\n ****************************************\n")
    print("Gasoline Branch")
    sleep(1)  # Simulating a brief pause
    gasActions[gasLevelIndicator]()  # Call the corresponding lambda function for the gas level

# Calling the gasLevelAlert function to check gas level and give feedback
gasLevelAlert()
