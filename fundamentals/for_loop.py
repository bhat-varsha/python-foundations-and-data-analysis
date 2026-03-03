"""
==================================================
FOR LOOP IN PYTHON
==================================================

A for loop is used to execute a block of code
repeatedly by iterating over a sequence.

It works with:
• List
• Tuple
• String
• Dictionary
• Set
• Range
• Any iterable object

Python’s for loop is called an "iterator-based loop"
because it directly fetches elements from a sequence,
without using manual indexing.

Syntax:
for variable in sequence:
    statements

Used for:
• Repeating code
• Reducing duplicate lines
• Iterating through collections
• Nested loops (used in patterns/graphics)
==================================================
"""
# ------------------------------------------------
# 1. Looping Through a List
# ------------------------------------------------
items = ["var", "sringeri", "reva", "bangalore"]
for name in items:
    print(name)
# Without loop (manual indexing)
print(items[0])
print(items[1])
print(items[2])
# ------------------------------------------------
# 2. Using range()
# ------------------------------------------------
# range(start, stop, step)
for number in range(1, 6):
    print(number)
for number in range(1, 10, 2):
    print(number)
# ------------------------------------------------
# 3. Looping Through a String
# ------------------------------------------------
for letter in "python":
    print(letter)
# ------------------------------------------------
# 4. Repeating a Statement
# ------------------------------------------------
for i in range(5):
    print("I am varsha")
# -----------------------------------------------
# 5. Even Numbers
# ------------------------------------------------
for number in range(2, 21, 2):
    print(number)

# ------------------------------------------------
# 6. Reverse Counting
# ------------------------------------------------
for x in range(10, 2, -2):
    print(x)

# This will not execute (wrong direction)
for y in range(2, 10, -2):
    print(y)