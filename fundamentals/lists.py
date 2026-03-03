"""
==================================================
PYTHON LISTS – COMPLETE GUIDE
==================================================

A list is a mutable (changeable), ordered, indexed
collection in Python that can store multiple values,
including different data types.

Key Features:
• Ordered
• Indexed
• Allows duplicates
• Mutable (can be modified)

Syntax:
list_name = [element1, element2, element3, ...]

--------------------------------------------------
Where Lists Are Used in Bioinformatics:
• Storing gene names
• Storing FASTA sequences
• Storing expression values from experiments
• Storing mutation positions
==================================================
"""


# ==================================================
# CREATING A LIST
# ==================================================

student = ["a", "b", "c", "d", 10, "10"]

print("Student list:", student)
print("Element at index 2:", student[2])   # Accessing element
print("Type of student:", type(student))
print("Element at index 5:", student[5])


# ==================================================
# UPDATING A LIST (Mutable Property)
# ==================================================

my_list = ["varsha", "var", "hosakere"]
print("Original list:", my_list)

my_list[0] = "sringeri"   # Updating value
print("Updated list:", my_list)


# ==================================================
# COMMON LIST METHODS
# ==================================================

students = ["a", "b", "c", "d"]
print("\nInitial students list:", students)

# Accessing
print("First element:", students[0])

# Updating
students[0] = "z"
print("After updating index 0:", students)

# append() → adds element at the end
students.append("varsha")
print("After append():", students)

# insert(index, value) → inserts at specific position
students.insert(1, "2")
print("After insert():", students)

# remove(value) → removes by value
students.remove("varsha")
print("After remove():", students)

# pop(index) → removes by index
students.pop(1)
print("After pop():", students)

"""
Difference between remove() and pop():

remove(value) → removes element using value
pop(index)    → removes element using index
"""


# ==================================================
# SORTING & REVERSING
# ==================================================

students.sort()   # Ascending order
print("Sorted list:", students)

students.reverse()   # Reverse order
print("Reversed list:", students)


# ==================================================
# LIST CONCATENATION
# ==================================================

a = ["1", "2", "3", "4", "5", "7"]
b = ["varsha", "varuna", "harvey", "mike", "mike", "joey"]
#i was watching suits ,thats the reason why harvey is here 

merge = a + b
print("Merged list:", merge)


# ==================================================
# OTHER USEFUL FUNCTIONS
# ==================================================

# count() → counts occurrences
print("Count of 'mike':", b.count("mike"))

# len() → length of list
print("Length of b:", len(b))

# clear() → removes all elements
a.clear()
print("List a after clear():", a)