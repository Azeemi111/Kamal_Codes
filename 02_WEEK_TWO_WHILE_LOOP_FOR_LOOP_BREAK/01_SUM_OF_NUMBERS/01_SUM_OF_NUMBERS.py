#-----------------------------------------------------------------------------
# Name:        Sum Of Numbers
# Purpose:     Calculating the sum of the users input
# Author:      Kamal Azeemi
# Created:     10-Mar-2025
# Updated:     11-Mar-2025
#-----------------------------------------------------------------------------
print("Number Calculator")
print() #space out the code
print("Input a number and this program will calculate the sum of its digits.")
#Store the users input
number = int(input("Please Enter A Number: "))

#State a variable and set it equal to 0
total = 0

#use a for loop to list numbers from 1 to the users input+1
for i in range(1, number+1):
    #add each number to the total
    total = total + i

print()
#print the output
print("The sum of numbers adding between themselves in range of 1 and",number,"is",total)
