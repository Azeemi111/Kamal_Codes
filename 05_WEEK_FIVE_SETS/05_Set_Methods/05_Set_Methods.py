# -----------------------------------------------------------------------------
# Challenge 5: Set Methods (Interactive)
# Concept: Using set methods like .copy(), .clear(), and .pop().
# Objective: Demonstrate various set methods.
# Author: Kamal
# Created: 13-Apr-2025
# -----------------------------------------------------------------------------

# Create the set
data_input = input("Enter numbers for your set (e.g. 10 20 30 40 50): ")
data = set(int(num) for num in data_input.split())

# Copy the set
data_copy = data.copy()
print("\nCopy:", data_copy)

# Pop an element
data.pop()
print("After pop:", data)

# Clear the set
data.clear()
print("After clear:", data)
