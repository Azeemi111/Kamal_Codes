# -----------------------------------------------------------------------------
# Name:        TUPLE BASICS
# Purpose:     Create a tuple with 5 different elements and access various parts of it
# Author:      Kamal Azeemi
# Created:     24-Mar-2025
# -----------------------------------------------------------------------------
# Introduction
print("\nWelcome to the Tuple Basics Program!")
print("You'll enter 5 values to create a tuple.\n")

# Loop to allow multiple runs
while True:
    # Get user input for the tuple
    int_element = int(input("Enter an integer: "))
    float_element = float(input("Enter a float: "))
    string_element = input("Enter a string: ")
    bool_element = input("Enter 'True' or 'False' for a boolean value: ").lower() == 'true'

    # Create a simple nested tuple
    nested_tuple = (1, 2, 3)

    # Create the main tuple
    my_tuple = (int_element, float_element, string_element, bool_element, nested_tuple)

    # 1. Print the entire tuple
    print("\nYour complete tuple is:", my_tuple)

    # 2. Access and print the third element
    print("The third element of your tuple is:", my_tuple[2])

    # 3. Extract the nested tuple and print its first element
    print("The first element of the nested tuple is:", my_tuple[4][0])

    # Ask if the user wants to run the program again
    more_tuples = input("\nDo you want to create another tuple? (yes/no): ").lower()

    if more_tuples != 'yes':
        break

# Final message
print("\nThanks for using the Tuple Basics Program!")
