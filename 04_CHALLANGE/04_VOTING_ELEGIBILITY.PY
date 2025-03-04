# -----------------------------------------------------------------------------
# Name:        Voting Eligibility
# Purpose:     Determining voting eligibility based off og age
# Author:      Kamal Azeemi
# Created:     2-Feb-2025
# Updated:     3-Mar-2025
# -----------------------------------------------------------------------------
print("Hello, this program will help determine if you a illegible to vote or not")
age = int(input("What is your age? "))
print()
print()
if age >= 18:
    print("\033[34mYou are able to vote!")
else:
    print("\033[31mYou're too young, go play outside! :))")
