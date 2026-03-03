#Control Statements in Python :Conditionals, Loops,
#Control statements control the flow of a program :
# they decide what runs, how many times it runs, and what to do if an error occurs.

#1.CONDITIONAL STATEMENTS (Decision Making) :Conditionals allow the program to make decisions.
#Keywords: if, elif, else
#Basic syntax
"""if condition:
    statement
elif condition:
    statement
else:
    statement
"""
#Example
x = 10
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")

#Multiple conditions
if x > 0 and x < 10:
    print("Single digit positive")

#Nested if
if x > 0:
    if x % 2 == 0:
        print("Positive even")
######################################################################
#2.LOOPS (Repetition) :Loops run code again and again until a condition stops it.
#for loop : When the number of iterations is known.
#Syntax
"""for item in iterable:
    statement
"""
#Examples
for i in range(5):
    print(i)

for base in "ATGC":
    print(base)

#range() function :range(start, stop, step)

#while loop: When the number of iterations is unknown.
#Syntax
"""
while condition:
    statement
"""
#Example
x = 5
while x > 0:
    x -= 1 #this step is very important
    print(x)

#Infinite loop (common error)
#while x > 0:
#    print(x) (no update to x)

#LOOP CONTROL STATEMENTS
#break – stop loop immediately
for i in range(10):
    if i == 5:
        break

#continue – skip current iteration
for i in range(5):
    if i == 2:
        continue
    print(i)

#pass – do nothing (placeholder)
if x > 0:
    pass


