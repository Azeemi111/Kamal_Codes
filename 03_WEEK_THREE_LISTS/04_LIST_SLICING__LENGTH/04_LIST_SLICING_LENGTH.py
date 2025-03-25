#-----------------------------------------------------------------------------
# Name:        LIST SLICING AND LENGTH
# Purpose:     Remove an item from a list.
# Author:      Kamal Azeemi
# Created:     19-Mar-2025
# Updated:     20-Mar-2025
#-----------------------------------------------------------------------------
print("\nThis program will slice a list of colors and find its length.\n")

# Create a variable for the list called colors
colors = ['red', 'blue', 'green', 'yellow', 'purple']

# Show the original list
print("The original list:", colors)

# Slice the list to get the second and third colors
sliced_colors = colors[1:3]

# Show the sliced list
print("\nThe sliced list with the second and third colors is:", sliced_colors)

# Find and print the length of the list
print("\nThe length of the original list is:", len(colors))

# Ask the user if they want to add more colors
new_colors = input("\nWould you like to add more colors? (yes/no): ")

if new_colors == 'yes' or new_colors == 'Yes':
    # Get the new colors from the user and split them by commas
    colors_to_add = input("Enter the colors to add, separated by commas: ").split(',')

    # Add the new colors to the list
    colors.extend([color.strip() for color in colors_to_add])
    print("\nThe new list is:", colors)
else:
    print("\nNo new colors added. The final list is:", colors)

print("\nThanks for using the Colors List Program!")
