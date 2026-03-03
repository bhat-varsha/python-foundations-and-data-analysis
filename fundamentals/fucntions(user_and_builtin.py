"""
==================================================
FUNCTIONS IN PYTHON
==================================================

A function is a block of reusable code that performs
a specific task.

Why use functions?
• Avoid repetition
• Improve readability
• Organize code properly
• Reuse logic easily

--------------------------------------------------
Types of Functions:

1. Built-in Functions (Already Defined)
   These are pre-defined in Python.
   Examples:
   print(), len(), type(), sum(), input(), etc.

2. User-Defined Functions
   Functions created by the programmer
   using the 'def' keyword.
==================================================
"""


# ==================================================
# 1. USER-DEFINED FUNCTION (With Return)
# ==================================================

def sub(x, y):
    return x - y

print("Subtraction:", sub(15, 20))


def add(a, b):
    return a + b

print("Addition:", add(10, 3))


# ==================================================
# 2. FUNCTION WITH PARAMETERS (No Return)
# ==================================================

def greet(name, age):
    print(f"{name} is {age} years old")

greet("varsha", 22)


# ==================================================
# 3. FUNCTION WITH USER INPUT
# ==================================================

def greet_user():
    name = input("What is your name? ")
    age = int(input("What is your age? "))
    print(f"{name} is {age} years old")

# Uncomment below line to run interactively
# greet_user()


# ==================================================
# 4. FUNCTION CALLING
# ==================================================

"""
Defining a function:
def function_name(parameters):
    statements

Calling a function:
function_name(arguments)

• Parameters → variables inside function definition
• Arguments → actual values passed while calling
"""


# ==================================================
# 5. EXAMPLE: LOOP INSIDE FUNCTION
# ==================================================

def battery_charge():
    battery = 60

    while battery < 100:
        battery += 10
        print("Battery level:", battery)

    print("Battery fully charged")

battery_charge()