import sys  # Importing sys to access system-specific parameters and functions
import time  # Importing time to control timing functions like sleep

print("\n\tWelcome to InfoTechCenter v1.0")  # Display a welcome message with a tab for formatting

x = 0  # Counter to control the loop
ellipses = 0  # Counter for the number of dots in the boot message

# A loop that simulates the system booting process
while x != 20:
    x += 1  # Increment the counter 'x' on each iteration
    # Create a message that shows booting status with an increasing number of dots
    message = ("InfoTech Center System Booting" + "." * ellipses)
    ellipses += 1  # Increment the number of ellipses (dots)

    # Print the message on the same line using sys.stdout.write and carriage return '\r' to overwrite the line
    sys.stdout.write("\r" + message)

    time.sleep(0.5)  # Pause the execution for 0.5 seconds to create the booting effect

    # Reset ellipses after 3 dots, so it cycles from 0 to 3
    if ellipses == 4:
        ellipses = 0

    # When the loop reaches 20 iterations, print the final message
    if x == 20:
        print("\n\n\n OS Booted Up - Retina Scanned - Access Granted")
