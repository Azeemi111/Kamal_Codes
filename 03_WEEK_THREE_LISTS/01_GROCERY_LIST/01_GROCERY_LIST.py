#-----------------------------------------------------------------------------
# Name:        Grocery List
# Purpose:     Create a list of groceries and then add new items to the list.
# Author:      Kamal
# Created:     18-Mar-2025
# Updated:     19-Mar-2025
#-----------------------------------------------------------------------------
print("\nThis program will list and add new items after one list is printed.\n")

# Create a variable for the list called grocery_list
grocery_list = ['apples', 'bread', 'milk', 'eggs']

# Show the original list
print("The original list:", grocery_list)

# Ask the user if they want to add more items
new_items = input("\nWould you like to add more items? (yes/no): ")

if new_items == 'yes' or new_items == 'Yes':
    # Get the new items from the user and split them by commas
    items_to_add = input("Enter the items to add, separated by commas: ").split(',')

    # Add the new items to the list
    grocery_list.extend(items_to_add)
    print("\nThe new list is:", grocery_list)
else:
    print("\nNo new items added. The final list is:", grocery_list)

print("\nThanks for using the Grocery List Program!")
