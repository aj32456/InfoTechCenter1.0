import sys
import time
import random

# ANSI color codes for various colors
colors = [
    "\033[91m",  # Red
    "\033[92m",  # Green
    "\033[93m",  # Yellow
    "\033[94m",  # Blue
    "\033[95m",  # Purple (Bright Magenta)
    "\033[96m",  # Cyan
    "\033[97m"  # White
]
reset_color = "\033[0m"  # Reset to default color

# Welcome message with each letter in a different random color
welcome_message = "Welcome to InfoTechCenter v1.0"
colored_welcome_message = []




# Loop through each letter and apply a random color
for letter in welcome_message:
    random_color = random.choice(colors)
    colored_welcome_message.append(f"{random_color}{letter}{reset_color}")

# Join the letters back together and print the colored welcome message
colored_welcome_message = ''.join(colored_welcome_message)
print(f"\n\t{colored_welcome_message}")  # The welcome message with each letter in a different color

timeToSleep = 3 #Variable to set the time library to 3 seconds when called
time.sleep(timeToSleep) #Calling the time to sleep library with the variable timeToSleep value

x = 0
ellipses = 0

# Simulate the booting process with different colors
while x != 20:
    x += 1

    # Randomly select a color for each iteration
    random_color = random.choice(colors)

    # Create the booting message with random color and ellipses
    message = (f"{random_color}InfoTech Center System Booting" + "." * ellipses + reset_color)
    ellipses += 1

    # Print the message with the random color on the same line
    sys.stdout.write("\r" + message)

    time.sleep(0.5)

    if ellipses == 4:
        ellipses = 0

    # After 20 iterations, print the final message
    if x == 20:
        final_message = "OS Booted Up - Retina Scanned - Access Granted"
        words = final_message.split()  # Split the final message into words
        colored_message = []

        # Loop through words and apply random colors to every other word
        for i, word in enumerate(words):
            if i % 2 == 0:
                colored_message.append(word)
            else:
                random_color = random.choice(colors)
                colored_message.append(f"{random_color}{word}{reset_color}")

        # Join the words back into a sentence
        colored_message = " ".join(colored_message)
        print(f"\n\n\n{colored_message}")  # Print the final message with alternating colors



print("\n***************************************\n")



print("\nWeather Branch\n")


# Import necessary libraries
import random  # For generating random weather conditions
from time import sleep  # For adding delays (to simulate time passing)


# Function to determine the weather condition
def weather():
    weatherForecast = ["snowy", "blizzard", "rainy", "windy", "icy", "Sunny"]  # List of possible weather conditions
    return random.choice(weatherForecast)  # Return the randomly chosen weather condition


# Call the weather function to get the current weather alert
weatherAlert = weather()


# Define a dictionary for weather responses and speed limits
weather_conditions = {
    "snowy": {"delay": 30, "speed_limit": 55},
    "blizzard": {"delay": 45, "speed_limit": 45},
    "rainy": {"delay": 15, "speed_limit": 65},
    "windy": {"delay": 10, "speed_limit": 70},
    "icy": {"delay": 50, "speed_limit": 30}
}


# Function to respond based on the weather condition
def vehicleResponseSystem():
    # Check if the weather condition is in the dictionary
    if weatherAlert in weather_conditions:
        condition = weather_conditions[weatherAlert]
        print(f"\nThe National Weather Service has delayed your alarm by {condition['delay']} minutes because"
              f" of the Forecasted {weatherAlert} weather conditions.")
        sleep(1)
        print(f"\nVRS System Has Been Engaged, restricting you to {condition['speed_limit']}-MPH.")
    else:
        # Handle clear or unlisted weather conditions
        print(f"\nThe National Weather Services has Called for {weatherAlert} Weather Conditions, Drive Carefully to get to your Destination!")
        sleep(1)
        print("\nVRS System Has  Disengaged.")


# Call the vehicle response system function to output the appropriate response
vehicleResponseSystem()


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

