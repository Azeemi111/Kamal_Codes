# -----------------------------------------------------------------------------
# Challenge 3: Adding and Removing Elements
# Concept: Using .add(), .remove(), and .discard() to modify sets.
# Objective: Add and remove elements from a set.
# Author: Kamal
# Created: 13-Apr-2025
# -----------------------------------------------------------------------------

# Create a set of numbers
numbers = {1, 2, 3, 4, 5}

# Add 6 and 7 to the set
numbers.add(6)
numbers.add(7)

# Remove 2 from the set
numbers.remove(2)  # Use .discard(2) if you want to avoid an error when the element is not present

# Print the updated set
print(numbers)
