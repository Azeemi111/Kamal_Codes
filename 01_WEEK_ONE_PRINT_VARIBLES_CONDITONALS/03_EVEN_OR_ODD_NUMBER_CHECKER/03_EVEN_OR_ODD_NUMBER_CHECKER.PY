#-----------------------------------------------------------------------------
# Name:        Even Or Odd Number Checker
# Purpose:     Determining if the number inputted is even or odd.
# Author:      Kamal Azeemi
# Created:     1-Mar-2025
# Updated:     2-Mar-2025
#-----------------------------------------------------------------------------
print("Hello, this code will help interpret if the number you type is even or odd")
number = int(input("Enter your number: ")) #Storeing users input by setting a variable
print() #Spacing out the code to make it look visually appealing
print()

if number % 2 == 0: #Executing different possibilities based off the users input
    print("\033[34mThe number you have inputted is even.")
else: #Setting a response if the user inputs a number different then the possibility listed above
    print("\033[31mThe number you have inputted is odd.")