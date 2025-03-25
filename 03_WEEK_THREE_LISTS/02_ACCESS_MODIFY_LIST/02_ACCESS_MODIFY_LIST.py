#-----------------------------------------------------------------------------
# Name:        ACCESS AND MODIFY LIST
# Purpose:     Modify a grocery list by changing an existing item.
# Author:      Kamal Azeemi
# Created:     19-Mar-2025
# Updated:     20-Mar-2025
#-----------------------------------------------------------------------------
print("\nThis program will modify a grocery list by changing an item and accessing another item.\n")

# Create a variable for the list called grocery_list
grocery_list = ['apples', 'bananas', 'carrots', 'milk', 'bread']

# Show the original list
print("The original list:", grocery_list)

# Modify 'bananas' to 'grapes'
grocery_list[1] = 'grapes'

# Show the updated list
print("\nThe updated list is:", grocery_list)

# Access and print the third item in the list
print("\nThe third item in the list is:", grocery_list[2])

# Ask the user if they want to add more items
new_items = input("\nWould you like to add more items? (yes/no): ")

if new_items == 'yes' or new_items == 'Yes':
    # Get the new items from the user and split them by commas
    items_to_add = input("Enter the items to add, separated by commas: ").split(',')

    # Add the new items to the list
    grocery_list.extend([item.strip() for item in items_to_add])
    print("\nThe new list is:", grocery_list)
else:
    print("\nNo new items added. The final list is:", grocery_list)

print("\nThanks for using the Grocery List Program!")

