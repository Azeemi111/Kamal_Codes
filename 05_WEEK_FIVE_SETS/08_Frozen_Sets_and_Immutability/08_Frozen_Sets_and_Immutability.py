# -----------------------------------------------------------------------------
# Challenge 8: Frozensets and Immutability (Interactive)
# Concept: Understanding the immutability of frozensets.
# Objective: Work with frozensets and understand immutability.
# Author: Kamal
# Created: 13-Apr-2025
# -----------------------------------------------------------------------------

# Ask the user to enter numbers
numbers = input("Enter numbers for frozenset: ")

# Create a frozenset
frozen_numbers = frozenset(numbers.split())

# Try to add an element (will fail)
print("\nTrying to add to a frozenset causes an error:")
print("Error: 'frozenset' object has no attribute 'add'")

# Print the frozenset
print("Frozenset:", frozen_numbers)
