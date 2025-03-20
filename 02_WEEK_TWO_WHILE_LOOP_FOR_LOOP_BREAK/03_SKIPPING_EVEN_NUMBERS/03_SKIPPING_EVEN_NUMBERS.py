# -----------------------------------------------------------------------------
# Name:        Skipping Even Numbers
# Purpose:     Displays all even numbers from the range of 1 to 10
# Author:      Kamal Azeemi
# Created:     12-Mar-2025
# Updated:     13-Mar-2025
# -----------------------------------------------------------------------------
#\n is used to space out code
print("\nHello, this program will print all even numbers between 1 and 10\n")
#Making the computer list numbers in range of 1 to 10
for i in range(1, 11):
    #Only if the number is divisible by two and leaves no remainders continue the next line of code
    if i % 2 == 0:
        print("\033[34m",i)
