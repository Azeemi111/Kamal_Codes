# -----------------------------------------------------------------------------
# Challenge 2: Accessing Set Elements (Interactive)
# Concept: Understanding that sets are unordered and unindexed.
# Objective: Use iteration to access elements in a set.
# Author: Kamal
# Created: 13-Apr-2025
# -----------------------------------------------------------------------------

# Ask the user to input colors
user_input = input("Enter colors separated by commas (e.g. red,blue,green): ")

# Create a set
colors = set(color.strip() for color in user_input.split(','))

# Loop through and print each color
print("\nYour colors are:")
for color in colors:
    print(color)
