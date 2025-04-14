# -----------------------------------------------------------------------------
# Challenge 3: Adding and Removing Elements (Interactive)
# Concept: Using .add(), .remove(), and .discard() methods to modify sets.
# Objective: Add and remove elements from a set.
# Author: Kamal
# Created: 13-Apr-2025
# -----------------------------------------------------------------------------

# Create a set from user input
initial_numbers = input("Enter numbers separated by spaces (e.g. 1 2 3 4 5): ")
numbers = set(int(num) for num in initial_numbers.split())

# Add numbers to the set
to_add = input("Enter two numbers to add to the set (e.g. 6 7): ")
numbers.update(int(n) for n in to_add.split())

# Remove a number from the set
to_remove = int(input("Enter a number to remove from the set: "))
numbers.discard(to_remove)

# Print the updated set
print("\nUpdated set:", numbers)
