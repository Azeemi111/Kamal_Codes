# -----------------------------------------------------------------------------
# Challenge 5: Set Methods
# Concept: Using set methods like .copy(), .clear(), and .pop().
# Objective: Demonstrate various set methods.
# Author: Kamal
# Created: 13-Apr-2025
# -----------------------------------------------------------------------------
# Create a set
data = {10, 20, 30, 40, 50}

# Copy the set
data_copy = data.copy()
print("Copy:", data_copy)

# Pop a random element (removes and returns an arbitrary item)
data.pop()
print("After pop:", data)

# Clear the set
data.clear()
print("After clear:", data)
