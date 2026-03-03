"""
==================================================
PYTHON VARIABLES & BASIC OPERATIONS
==================================================

A variable is a name given to a memory location
that stores data or values.

Variables are like containers that store data,
which can be used and changed during program execution.

Python variables are dynamically typed:
The data type is decided automatically based
on the value assigned.

Syntax:
variable_name = value
==================================================
"""


# ==================================================
# BASIC OPERATIONS
# ==================================================

# Integer data type
a = 6
b = 3
print("a + b =", a + b)

c, d = 5, 3
print("c - d =", c - d)

# String data type
name = "varsha"
print("Name:", name)


# ==================================================
# MULTIPLE ASSIGNMENT
# ==================================================

a, b = 2, 3
print("Before swapping:", a, b)

# Swapping variables
a, b = b, a
print("After swapping:", a, b)


# ==================================================
# VARIABLE RULES
# ==================================================

"""
Rules for naming variables:

1. Must start with a letter (a–z, A–Z) or underscore (_)
2. Cannot start with a number
3. Cannot contain special characters except underscore (_)
4. Case sensitive (age and Age are different variables)
5. No spaces allowed

Examples of valid variables:
name = "varsha"
_course = "Bioinformatics"

Invalid examples:
2name = "varsha"      ❌
name@ = "varsha"      ❌
"""


# ==================================================
# EXAMPLE VARIABLES
# ==================================================

name = "varsha"
course = "MSc Bioinformatics"

print("Student Name:", name)
print("Course:", course)