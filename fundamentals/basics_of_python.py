"""⭐
1. PYTHON SYNTAX=
Python syntax refers to the set of rules that define how Python code must be written
and formatted—such as indentation, naming, statements, blocks, etc.

python is a case sensitive
free and open source python
has cross compatibility
general purpose lanaguage
Key Points:
Python uses indentation instead of braces {}.
Statements end automatically (no semicolon required).
Case-sensitive language.

line by line intrepretor not a compile language
Python executes the program one line at a time, from top to bottom
It does NOT convert the entire program into machine code at once (like C, C++, Java do).
Instead, the Python interpreter reads one line → converts it → executes it immediately.
advantage of line by line interpretor is
1. easy to debug;
Python will stop there  at error in that line and show the error,
even if the lines after that are correct.
2.quick testing


#syntax =basic structure of programme
a= 10
#in this a is constant not variable becaues it ramains constant

"""
x = 10       # variable
if x > 5:    # indentation
    print("Greater")

#example to show python is line by line inertpretor
print("Line 1")
print("Line 2")
#print(line 3)   # Error here
print("Line 4")
#the code stop at 29 line showing errro
