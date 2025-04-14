# Challenge 8: Frozen Sets and Immutability

## Concept
Frozensets are immutable versions of sets in Python. Once created, you cannot modify a frozenset by adding or removing elements.

## Objective
Understand and work with frozensets to observe their immutability.

## Task
- Create a frozenset: `frozen_numbers = frozenset({1, 2, 3, 4, 5})`
- Attempt to add an element to the frozenset (this should raise an error).
- Print the frozenset.

## Example Output
```python
Error: 'frozenset' object has no attribute 'add'
{1, 2, 3, 4, 5}
