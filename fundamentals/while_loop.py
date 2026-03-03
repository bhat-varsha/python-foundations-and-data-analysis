"""
==================================================
WHILE LOOP IN PYTHON
==================================================

A while loop repeatedly executes a block of code
as long as the given condition is True.

Difference Between for and while:

For Loop:
• Used when the number of iterations is known
• Often used with range() or sequences

While Loop:
• Used when the number of iterations is unknown
• Runs until the condition becomes False
• Condition is checked before every iteration

Syntax:
while condition:
    statements

Important:
• Update the variable inside the loop
• Otherwise, it may create an infinite loop
==================================================
"""
# ------------------------------------------------
# 1. Basic While Loop
# ------------------------------------------------
i = 1
while i <= 5:
    print(i)
    i += 1   # Increment to avoid infinite loop , which is very important
# ------------------------------------------------
# 2. Reverse Counting Using for Loop
# ------------------------------------------------
for x in range(10, 2, -2):
    print(x)
# ------------------------------------------------
# 3. Reverse Counting Using while Loop
# ------------------------------------------------
i = 10
while i >= 0:
    print(i)
    i -= 2