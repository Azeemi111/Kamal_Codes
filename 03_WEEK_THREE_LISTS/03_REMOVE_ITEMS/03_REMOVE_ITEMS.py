#-----------------------------------------------------------------------------
# Name:        REMOVE ITEMS FROM LIST
# Purpose:     Remove an item from a list.
# Author:      Kamal
# Created:     19-Mar-2025
# Updated:     20-Mar-2025
#-----------------------------------------------------------------------------
print("\nThis program will modify a to-do list by removing items.\n")

# Create a variable for the list called todo_list
todo_list = ['write email', 'finish homework', 'call mom', 'clean room']

# Show the original list
print("The original list:", todo_list)

# Remove 'call mom' from the list
todo_list.remove('call mom')

# Show the updated list
print("\nThe updated list after removing 'call mom' is:", todo_list)

# Remove 'clean room' from the list
todo_list.remove('clean room')

# Show the final list
print("\nThe final list after removing 'clean room' is:", todo_list)

# Ask the user if they want to add more items
new_items = input("\nWould you like to add more items? (yes/no): ")

if new_items == 'yes' or new_items == 'Yes':
    # Get the new items from the user and split them by commas
    items_to_add = input("Enter the items to add, separated by commas: ").split(',')

    # Add the new items to the list
    todo_list.extend([item.strip() for item in items_to_add])
    print("\nThe new list is:", todo_list)
else:
    print("\nNo new items added. The final list is:", todo_list)

print("\nThanks for using the To-Do List Program!")
