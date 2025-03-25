#-----------------------------------------------------------------------------
# Name:        REMOVE ITEMS FROM LIST
# Purpose:     Remove an item from a list.
# Author:      Kamal Azeemi
# Created:     19-Mar-2025
# Updated:     20-Mar-2025
#-----------------------------------------------------------------------------
print("\nThis program will create a list of even numbers and their squares.\n")

# Create a variable for the list called numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Show the original list
print("The original list:", numbers)

# Create a list of even numbers
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

# Show the list of even numbers
print("\nThe list of even numbers is:", even_numbers)

# Create a list of squares of the even numbers
squared_numbers = []
for num in even_numbers:
    squared_numbers.append(num ** 2)

# Show the list of squared numbers
print("\nThe list of squares of even numbers is:", squared_numbers)

print("\nThanks for using the Number Filtering Program!")
