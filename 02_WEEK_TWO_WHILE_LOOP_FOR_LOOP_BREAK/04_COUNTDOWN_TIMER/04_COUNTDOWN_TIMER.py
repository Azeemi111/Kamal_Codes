# -----------------------------------------------------------------------------
# Name:        Countdown Timer
# Purpose:     Counts down from 10 to 1 and asks the user if they would like to stop the program each time it counts one value down.
# Author:      Kamal Azeemi
# Created:     14-Mar-2025
# Updated:     15-Mar-2025
# -----------------------------------------------------------------------------
#Pulling information from a library called time to the code
import time

print("\nI will countdown from 10 to 1, tell me when to stop by typing the command 'Stop': \n")
#Setting a variable to a value of 10
counter = 10

#Creating a while true loop to list numbers if greater than 0
while counter > 0:
    print(counter)
    #Asking the user if they wish to end the countdown
    user = input("Type 'Stop' if you want end the countdown otherwise type 'No': ")
    if user == "Stop" or user == "stop" or user == "STOP":
        #Ends the code completely
        break
    #Subtracts 1 from the counter each time the user wishes to continue
    counter -= 1
    #Adds a 1 seconds delay to display the next number
    time.sleep(1)
else:
    print("Countdown has been completed")
