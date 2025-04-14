# -----------------------------------------------------------------------------
# Challenge 7: Sets vs Lists (Interactive)
# Concept: Understanding the key differences between sets and lists.
# Objective: Compare the behavior of sets and lists.
# Author: Kamal
# Created: 13-Apr-2025
# -----------------------------------------------------------------------------

# Ask the user to enter numbers for the list
numbers = input("Enter numbers (duplicates allowed): ")

# Create the list
num_list = numbers.split()

# Convert the list to a set
num_set = set(num_list)

# Print both
print("\nList:", num_list)
print("Set:", num_set)
