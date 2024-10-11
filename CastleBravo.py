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


