# -----------------------------------------------------------------------------
# Name:        TUPLE OPERATIONS & COUNT
# Purpose:     Count the occurrences of a fruit in a tuple
# Author:      Kamal
# Created:     24-Mar-2025
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Name:        TUPLE OPERATIONS & COUNT
# Purpose:     Count the occurrences of a fruit in a tuple with repeated values
# Author:      Kamal Azeemi
# Created:     24-Mar-2025
# -----------------------------------------------------------------------------
# Create a tuple with repeated values
fruits_tuple = ("apple", "banana", "apple", "cherry", "banana", "apple")

# Introduction
print("\nWelcome to the Tuple Operations & Count Program!")
print("You'll input a fruit name, and the program will tell you how many times it appears in the tuple.\n")

# Loop to allow multiple fruit count checks
while True:
    # Ask the user to enter a fruit name
    fruit_name = input("Enter a fruit name: ")

    # Count the occurrences of the entered fruit in the tuple
    fruit_count = fruits_tuple.count(fruit_name)

    # Print the result
    print("\n",fruit_name,"appears at",fruit_count, "times in the tuple.")

    # Ask if the user wants to check for more fruits
    more_fruits = input("\nDo you want to check for another fruit? (yes/no): ").lower()

    if more_fruits != 'yes':
        break

# Final message
print("\nThanks for using the Tuple Operations & Count Program!")
