"""
==================================================
PYTHON INDEXING & SLICING
==================================================

Indexing:
Accessing individual elements using position number.

Forward indexing → starts at 0
Negative indexing → starts at -1
Stop index is always excluded.
Syntax: sequence[start : stop : step]
==================================================
"""

# ==================================================
# STRING INDEXING
# ==================================================

text = "Varsha_hosakere"

print("Length:", len(text))
print("First character:", text[0])
print("text[0:5]:", text[0:5])
print("text[0:9:2]:", text[0:9:2])


# ==================================================
# NEGATIVE INDEXING
# ==================================================

numbers = [0,1,2,3,4,5,6,7,8,9]

print("Last element:", numbers[-1])
print("numbers[-5:-1]:", numbers[-5:-1])
print("Reverse slice:", numbers[-1:-5:-1])


# ==================================================
# STRING SLICING EXAMPLES
# ==================================================

college = "reva_university"

print("college[0:4]:", college[0:4])
print("Full string:", college[:])
print("Reverse string:", college[::-1])
print("college[:-1]:", college[:-1])


# ==================================================
# LIST METHODS + SLICING
# ==================================================

nums = [1, 2, 3, 4, 5]

print("Original list:", nums)

nums.reverse()
print("After reverse():", nums)

nums.sort()
print("After sort():", nums)

print("Reverse using slicing:", nums[::-1])