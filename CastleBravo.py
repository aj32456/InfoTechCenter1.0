# Printing a visual separator for the output
print("\n ****************************************\n")

# Printing the name of the branch or section of the program
print("Gasoline Branch")

# Importing required modules
import random  # For random selection from lists and generating random numbers
from time import sleep  # For pausing the program's execution (simulating real-time delays)


# Function to randomly select a gas level
def gasLevelGaugue():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank",
                    "Full Tank"]  # Possible gas levels
    return random.choice(gasLevelList)  # Randomly returns one gas level from the list


# Function to randomly select a gas station
def gasStations():
    gasStationsList = ["BP", "Shell", "Meijer", "Sams club", "Marathon", "Mobile", "Speedway",
                       "Circle K"]  # List of gas stations
    return random.choice(gasStationsList)  # Randomly returns one gas station from the list


# Function to alert the user based on the gas level
def gasLevelAlert():
    # Random distances to the closest gas station, depending on gas levels
    milesToGasStationLow = round(random.uniform(1, 25), 1)  # Random distance if the gas level is "Low"
    milesToGasSTationQuarterTank = round(random.uniform(25.1, 50),
                                         1)  # Random distance if the gas level is "Quarter Tank"

    gasLevelIndicator = gasLevelGaugue()  # Getting the current gas level using the gasLevelGaugue function

    # Checking the gas level and responding accordingly
    if gasLevelIndicator == "Empty":
        print("\n***WARNING - YOU ARE ON EMPTY***\n")
        sleep(2)  # Pausing for 2 seconds to simulate processing
        print("Calling Triple AAA")  # Emergency situation: need to call for help
    elif gasLevelIndicator == "Low":
        print("Your Gas Tank Is Extremely Low, Checking GPS for The Closest Gas Station")
        sleep(2)  # Pausing for 2 seconds to simulate checking GPS
        print("The Closest Gas Station is", gasStations(), "Which is", milesToGasStationLow,
              "Miles Away")  # Suggesting a nearby gas station
    elif gasLevelIndicator == "Quarter Tank":
        print("Your Gas Tank Is a Quarter of a Tank, Checking GPS for The Closest Gas Station")
        sleep(2)  # Pausing for 2 seconds to simulate checking GPS
        print("The Closest Gas Station is", gasStations(), "Which is", milesToGasSTationQuarterTank,
              "Miles Away")  # Suggesting a nearby gas station
    elif gasLevelIndicator == "Half Tank":
        print(
            "Your Gas Tank is Half-way Empty, which leaves plenty to get to your Destination.")  # No immediate need to refuel
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your Gas Tank is 3/4 full, which leaves plenty to get to your Destination.")  # Ample gas left
    else:
        print("Your Gas Tank is Full!")  # Full tank, no worries about refueling


# Calling the gasLevelAlert function to check the gas level and provide appropriate feedback
gasLevelAlert()
