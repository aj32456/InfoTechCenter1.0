print("\n***************************************\n")  # Prints a separator for better formatting
print("Weather Branch\n")  # Prints a header to introduce the weather section

# Import necessary libraries
import random  # For generating random weather conditions
from time import sleep  # For adding delays (to simulate time passing)

# Function to determine the weather condition
def weather():
    weatherForecast = ["snowy", "blizzard", "rainy", "windy", "icy", "Sunny"]  # List of possible weather conditions
    weatherCondition = random.choice(weatherForecast)  # Randomly choose one of the weather conditions
    return weatherCondition  # Return the chosen weather condition

# Call the weather function to get the current weather alert
weatherAlert = weather()

# Function to respond based on the weather condition
def vehicleResponseSystem():
    # Check if the weather is snowy
    if weatherAlert == "snowy":
        print("\n The National Weather Service has updated alarm by 30 minutes because"
              " of the Forecast of", weatherAlert, "weather conditions.")  # Notify about snow and delay
        sleep(1)  # Pause for 1 second
        print("\n VRS System Has Been Engaged, Only Allowing You to Drive 55-MPH.")  # Limit speed to 55-MPH

    # Check if the weather is a blizzard
    elif weatherAlert == "blizzard":
        print("\n The National Weather Service has updated alarm by 45 minutes because"
              " of the Forecast of", weatherAlert, "weather conditions.")  # Notify about blizzard and delay
        sleep(1)  # Pause for 1 second
        print("\n VRS System Has Been Engaged, Only Allowing You to Drive 45-MPH.")  # Limit speed to 45-MPH

    # Check if the weather is rainy
    elif weatherAlert == "rainy":
        print("\n The National Weather Service has updated alarm by 15 minutes because"
              " of the Forecast of", weatherAlert, "weather conditions.")  # Notify about rain and delay
        sleep(1)  # Pause for 1 second
        print("\n VRS System Has Been Engaged, Only Allowing You to Drive 65-MPH.")  # Limit speed to 65-MPH

    # Check if the weather is windy
    elif weatherAlert == "windy":
        print("\n The National Weather Service has updated alarm by 10 minutes because"
              " of the Forecast of", weatherAlert, "weather conditions.")  # Notify about wind and delay
        sleep(1)  # Pause for 1 second
        print("\n VRS System Has Been Engaged, Only Allowing You to Drive 70-MPH.")  # Limit speed to 70-MPH

    # Check if the weather is icy
    elif weatherAlert == "icy":
        print("\n The National Weather Service has updated alarm by 50 minutes because"
              " of the Forecast of", weatherAlert, "weather conditions.")  # Notify about ice and delay
        sleep(1)  # Pause for 1 second
        print("\n VRS System Has Been Engaged Only Allowing You to Drive 30-MPH.")  # Limit speed to 30-MPH

    # For sunny or other weather conditions
    else:
        print("\n The National Weather Service is Calling for", weatherAlert,
              "Skies, Drive Carefully to get to your Destination!")  # Notify about clear skies and careful driving
        sleep(1)  # Pause for 1 second
        print("\n VRS System Has Been Disengaged.")  # No speed restrictions

# Call the vehicle response system function to output the appropriate response
vehicleResponseSystem()
