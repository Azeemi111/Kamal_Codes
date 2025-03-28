# -----------------------------------------------------------------------------
# Name:        SWAP VALUES PROGRAM
# Purpose:     Swap two numbers input by the user without using a temporary variable
# Author:      Kamal Azeemi
# Created:     24-Mar-2025
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Name:        SWAPPING VALUES USING TUPLES
# Purpose:     Swap two numbers input by the user without using a temporary variable
# Author:      Kamal
# Created:     24-Mar-2025
# -----------------------------------------------------------------------------
# Introduction
print("\nWelcome to the Swapping Values Using Tuples Program!")
print("You'll input two numbers, and the program will swap their values.\n")

# Loop to allow multiple swaps
while True:
    # Get user input for the two numbers
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))

    # Store the numbers in a tuple
    numbers_tuple = (first_number, second_number)

    # Swap the values using tuple unpacking (no temporary variable)
    swapped_values = (numbers_tuple[1], numbers_tuple[0])

    # Print the swapped values
    print(f"\nSwapped values: {swapped_values}")

    # Ask if the user wants to swap more values
    more_swaps = input("\nDo you want to swap more values? (yes/no): ").lower()

    if more_swaps != 'yes':
        break

# Final message
print("\nThanks for using the Swapping Values Using Tuples Program!")
