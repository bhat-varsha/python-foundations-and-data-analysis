"""
===========================================
CONTROL FLOW – CONDITIONAL STATEMENTS
===========================================

Conditional statements control program flow
by executing code based on conditions.

Types:
• if    → executes if condition is True
• elif  → checks another condition
• else  → executes if all conditions are False

Indentation is very important in Python.
"""

# ------------------------------------------------
# 1. Basic if-else
# ------------------------------------------------

num = -5

if num > 0:
    print("Positive number")
else:
    print("Negative number or zero")


# ------------------------------------------------
# 2. if-elif-else (Multiple Conditions)
# ------------------------------------------------

marks = 76

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# ------------------------------------------------
# 3. Using Logical Operators
# ------------------------------------------------

age = 25

if age > 18 and age < 60:
    print("Eligible")


# ------------------------------------------------
# 4. Nested if
# ------------------------------------------------

score = 95

if score >= 40:
    if score >= 90:
        print("Distinction")


# ------------------------------------------------
# 5. Boolean Condition
# ------------------------------------------------

is_active = True

if is_active:
    print("Active user")