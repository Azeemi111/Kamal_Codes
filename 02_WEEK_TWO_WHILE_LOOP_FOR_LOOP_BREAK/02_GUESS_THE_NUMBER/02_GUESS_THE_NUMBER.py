#-----------------------------------------------------------------------------
# Name:        Guess The Number
# Purpose:     Fun game for the user to guess what number the computer is thinking about from the range of 1 to 10
# Author:      Kamal Azeemi
# Created:     11-Mar-2025
# Updated:     12-Mar-2025
#-----------------------------------------------------------------------------
#Pulling information from a library called random to implement in the code
import random
print("Guess The Number Game!\n")
print("Choose a number between 1 and 10.\n\n")
#Storeing the users input
user = int(input("What is your guess? "))
#Making the computer pick a random number in the range of 1 to 10
guess = random.randint(1, 11)
#If the users guess matches the random number selected by the computer continue the code
if user == guess:
    print("\033[34mCorrect!")
#If the numbers do not match run this section of the code
else:
    print("\033[31mSorry, the guess is incorrect.")