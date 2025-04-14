# -----------------------------------------------------------------------------
# Challenge 6: Adding and Removing Elements (Using Update and Discard)
# Concept: Using .update() and .discard() for bulk modifications.
# Objective: Modify a set efficiently.
# Author: Kamal
# Created: 13-Apr-2025
# -----------------------------------------------------------------------------
# Create a set of letters
letters = {'a', 'b', 'c'}

# Add multiple elements using .update()
letters.update(['d', 'e', 'f'])

# Remove 'b' using .discard()
letters.discard('b')

# Print the updated set
print(letters)
