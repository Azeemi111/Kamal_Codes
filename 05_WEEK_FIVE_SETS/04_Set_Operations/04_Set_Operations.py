# -----------------------------------------------------------------------------
# Challenge 4: Set Operations (Interactive)
# Concept: Performing set operations like union, intersection, and difference.
# Objective: Combine and compare sets using set operations.
# Author: Kamal
# Created: 13-Apr-2025
# -----------------------------------------------------------------------------

# Create two sets from user input
set1_input = input("Enter numbers for Set 1 (e.g. 1 2 3 4): ")
set2_input = input("Enter numbers for Set 2 (e.g. 3 4 5 6): ")

set1 = set(int(num) for num in set1_input.split())
set2 = set(int(num) for num in set2_input.split())

# Perform operations
print("\nUnion:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference (Set1 - Set2):", set1.difference(set2))
