# -----------------------------------------------------------------------------
# Challenge 8: Frozen Sets and Immutability
# Concept: Understanding the immutability of frozensets.
# Objective: Work with frozensets and understand immutability.
# Author: Kamal
# Created: 13-Apr-2025
# -----------------------------------------------------------------------------
# Create a frozenset
frozen_numbers = frozenset({1, 2, 3, 4, 5})

# Attempt to add an element (this will cause an error because frozensets are immutable)
try:
    frozen_numbers.add(6)
except AttributeError as e:
    print("Error:", e)

# Print the frozenset
print(frozen_numbers)
