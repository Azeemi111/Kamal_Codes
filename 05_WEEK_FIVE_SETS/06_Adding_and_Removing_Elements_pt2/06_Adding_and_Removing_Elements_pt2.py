# -----------------------------------------------------------------------------
# Challenge 6: Adding and Removing Elements (Using Update and Discard)
# Concept: Using .update() and .discard() for bulk modifications.
# Objective: Modify a set efficiently.
# Author: Kamal
# Created: 13-Apr-2025
# -----------------------------------------------------------------------------

# Create the initial set
initial_input = input("Enter some letters separated by spaces (e.g. a b c): ")
letters = set(initial_input.split())

# Add more letters
more_input = input("Enter more letters to add (e.g. d e f): ")
letters.update(more_input.split())

# Remove a letter
to_discard = input("Enter a letter to discard: ").strip()
letters.discard(to_discard)

# Print the updated set
print("\nUpdated letters set:", letters)
