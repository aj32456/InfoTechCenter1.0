print("\n***************************************\n")
print("Weather Branch\n")

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
        print(f"\nThe National Weather Service has updated alarm by {condition['delay']} minutes because"
              f" of the Forecast of {weatherAlert} weather conditions.")
        sleep(1)
        print(f"\nVRS System Has Been Engaged, Only Allowing You to Drive {condition['speed_limit']}-MPH.")
    else:
        # Handle clear or unlisted weather conditions
        print(f"\nThe National Weather Service is Calling for {weatherAlert} Skies, Drive Carefully to get to your Destination!")
        sleep(1)
        print("\nVRS System Has Been Disengaged.")

# Call the vehicle response system function to output the appropriate response
vehicleResponseSystem()
