#-----------------------------------------------------------------------------
# Name:        Grocery List
# Purpose:     Create a list of groceries and then add new items to the list.
# Author:      Kamal Azeemi
# Created:     18-Mar-2025
# Updated:     19-Mar-2025
#-----------------------------------------------------------------------------
print("\nThis program will list and add new items after one list is printed\n")
#Create a variable for lists called grocery_lists
grocery_list = ['apples', 'bread', 'milk', 'eggs']
#Create a variable for lists called grocery_lists
print("The original list",grocery_list)
grocery_list.extend(['cheese', 'tomatoes'])
print("The new list is",grocery_list)
