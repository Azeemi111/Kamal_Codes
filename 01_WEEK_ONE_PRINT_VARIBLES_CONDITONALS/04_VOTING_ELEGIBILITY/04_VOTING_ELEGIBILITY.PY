# -----------------------------------------------------------------------------
# Name:        Voting Eligibility
# Purpose:     Determining voting eligibility based off og age
# Author:      Kamal Azeemi
# Created:     2-Feb-2025
# Updated:     3-Mar-2025
# -----------------------------------------------------------------------------
print("Hello, this program will help determine if you a illegible to vote or not")
age = int(input("What is your age? ")) #Storeing users input by setting a variable
print() #Spacing out the code to make it look visually appealing
print()
if age >= 18: #Executing different possibilities based off the users input
    print("\033[34mYou are able to vote!")
else: #Setting a response if the user inputs a number different then the possibility listed above
    print("\033[31mYou're too young, go play outside! :))")
