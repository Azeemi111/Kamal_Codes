# -----------------------------------------------------------------------------
# Challenge 1: Creating Sets (Interactive)
# Concept: Understanding how to define and initialize sets.
# Objective: Create and print a set with unique elements.
# Author: Kamal
# Created: 13-Apr-2025
# -----------------------------------------------------------------------------

# Ask the user to enter fruit names separated by commas
user_input = input("Enter 3 fruits separated by commas (e.g. apple,banana,cherry): ")

# Create a set with the elements entered by the user
fruits = set(fruit.strip() for fruit in user_input.split(','))

# Print the set
print("\nYour new fruit set is:", fruits)
