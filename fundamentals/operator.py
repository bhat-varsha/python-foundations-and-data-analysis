"""
==================================================
PYTHON OPERATORS – COMPLETE REVISION NOTES
==================================================

An operator is a symbol that performs an operation
on one or more operands (values or variables)
and produces a result.

Operators are used for:
• Mathematical calculations
• Comparisons
• Logical decisions
• Assignments
• Bit-level operations
• Identity checking
• Membership testing

NOTE:
=  → Assignment operator
== → Comparison operator
==================================================
"""


# ==================================================
# 1. ARITHMETIC OPERATORS
# ==================================================
"""
Used for mathematical calculations.

+   Addition              → a + b
-   Subtraction           → a - b
*   Multiplication        → a * b
/   Division (float)      → a / b
//  Floor Division        → a // b
%   Modulus (remainder)   → a % b
**  Exponent (power)      → a ** b
"""

a, b, c = 10, 12, 2

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division (float):", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** c)


# ==================================================
# 2. RELATIONAL / COMPARISON OPERATORS
# ==================================================
"""
Used to compare two values.
Output is always Boolean (True or False).

==   Equal to
!=   Not equal to
>    Greater than
<    Less than
>=   Greater than or equal to
<=   Less than or equal to
"""

a, b, c = 10, 12, 2
d, e, f = 10, 12, 2

print("a < b:", a < b)
print("b > c:", b > c)
print("b <= e:", b <= e)
print("b == c:", b == c)
print("b >= e:", b >= e)
print("a != b:", a != b)


# ==================================================
# 3. LOGICAL OPERATORS
# ==================================================
"""
Used to combine conditions.

and  → True if both conditions are True
or   → True if at least one condition is True
not  → Reverses the condition
"""

print("c < d OR a > b:", c < d or a > b)
print("a > c AND a < b:", a > c and a < b)

value = True
print("NOT value:", not value)


# ==================================================
# 4. ASSIGNMENT OPERATORS
# ==================================================
"""
Used to assign values to variables.

=    Assign
+=   Add and assign
-=   Subtract and assign
*=   Multiply and assign
/=   Divide and assign
%=   Modulus and assign
//=  Floor divide and assign
**=  Power and assign
"""

a = 10
a += 12
print("a after += :", a)

b = 10
b -= 20
print("b after -= :", b)

c = 26
c /= 2
print("c after /= :", c)

d = 30
d %= 4
print("d after %= :", d)

e = 7
e *= 3
print("e after *= :", e)

f = 5
f **= 2
print("f after **= :", f)


# ==================================================
# 5. BITWISE OPERATORS
# ==================================================
"""
Operate at binary (bit) level.

&   Bitwise AND
|   Bitwise OR
^   Bitwise XOR
~   Bitwise NOT
<<  Left Shift
>>  Right Shift
"""

x = 5   # 0101
y = 3   # 0011

print("x & y:", x & y)
print("x | y:", x | y)
print("x ^ y:", x ^ y)
print("~x:", ~x)
print("x << 1:", x << 1)
print("x >> 1:", x >> 1)


# ==================================================
# 6. IDENTITY OPERATORS
# ==================================================
"""
Check whether two variables refer to the same object in memory.

is      → True if both refer to same object
is not  → True if they refer to different objects
"""

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("a is b:", a is b)         # True
print("a is c:", a is c)         # False
print("a is not c:", a is not c)


# ==================================================
# 7. MEMBERSHIP OPERATORS
# ==================================================
"""
Check whether a value exists in a sequence.

in
not in
"""

fruits = ["apple", "banana", "mango"]

print("apple in fruits:", "apple" in fruits)
print("orange in fruits:", "orange" in fruits)
print("grapes not in fruits:", "grapes" not in fruits)
print("banana not in fruits:", "banana" not in fruits)
