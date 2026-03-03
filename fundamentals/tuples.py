"""
==================================================
PYTHON TUPLES (and Basic Set Comparison)
==================================================

A tuple is an ordered, indexed, immutable collection
in Python that stores multiple values inside parentheses ().

Key Features:
• Ordered
• Indexed
• Allows duplicates
• Immutable (cannot be changed after creation)
• Faster than lists (generally)

Syntax:
tuple_name = (element1, element2, element3)

Example of immutability:
t[1] = 50   ❌ TypeError

--------------------------------------------------
Where Tuples Are Used in Bioinformatics:
• Storing genetic code tables
• Chromosome coordinates
• Fixed biological constants
• Returning multiple values from functions
==================================================
"""


# ==================================================
# CREATING A TUPLE
# ==================================================

mytuple1 = (1, 2, 3, 4, "Var")

print("Type:", type(mytuple1))
print("First Element:", mytuple1[0])
print("Slicing (first 3 elements):", mytuple1[:3])
print("Length:", len(mytuple1))


# ==================================================
# CONCATENATION (Works for both tuples and lists)
# ==================================================

mytuple2 = ("Varun", "shree", "varsh")
combined_tuple = mytuple1 + mytuple2

print("Combined Tuple:", combined_tuple)


# ==================================================
# REPEATING A TUPLE
# ==================================================

repeated_tuple = mytuple1 * 3
print("Repeated Tuple:", repeated_tuple)


# ==================================================
# TUPLE FUNCTIONS
# ==================================================

mytuple = (1, 2, 3, 4, 5)

print("Sum:", sum(mytuple))
print("Max:", max(mytuple))
print("Min:", min(mytuple))

"""
Tuple-specific methods:
• count(value)
• index(value)
"""

mytuple3 = (1, 2, 3, 4, 5, 6, 6)

print("Count of 6:", mytuple3.count(6))
print("Index of 3:", mytuple3.index(3))


# ==================================================
# IMMUTABILITY DEMONSTRATION
# ==================================================

var = (2.3, 5.3)
print("Tuple:", var)

# vivek[0] = 1   ❌ TypeError (Tuples are immutable)


# ==================================================
# CONVERTING TUPLES
# ==================================================

mytuple4 = (1, 2, 3, 4, 5)

tuple_to_set = set(mytuple4)
tuple_to_list = list(mytuple4)

print("Tuple to Set:", type(tuple_to_set))
print("Tuple to List:", type(tuple_to_list))

tuple_list = [("a", 1), ("b", 2), ("c", 3)]
tuple_to_dict = dict(tuple_list)

print("Tuple list to Dictionary:", type(tuple_to_dict))


# ==================================================
# COMPARISON: LIST vs TUPLE vs SET
# ==================================================

my_tuple = (1, 2, 3, 4, 5, 6, 6)
print("Tuple:", my_tuple)

my_list = [1, 2, 3, 1, 1]
print("List:", my_list)

my_set = {3, 1, 1, 2, 2}
print("Set (duplicates removed):", my_set)

"""
Important Differences:

List:
• Ordered
• Mutable
• Allows duplicates

Tuple:
• Ordered
• Immutable
• Allows duplicates

Set:
• Unordered
• No duplicates
• Cannot access by index
"""