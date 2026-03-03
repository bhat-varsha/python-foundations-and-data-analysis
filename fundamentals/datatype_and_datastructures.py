"""
Data type = type of data stored in a variable.
A data type defines the kind of value a variable can store and what operations can be performed on it.
It decides how Python will treat that data
They decide memory size required
They determine which operations are allowed

numbers:Numeric values used for math operations.
syntax\
#subtypes of numeric data types
a = 10      # int
b = 3.14    # float
c = 2 + 3j  # complex

strings:A sequence of characters inside quotes.
"hello"
'hello'

 Boolean:Stores truth values: True or False.
Used in conditions and decision making.

Example
is_student = True
print(is_student)

Syntax
flag = True
prgrm :
x = 5
print(x > 3)
"""

"""
data structres are collection data types.
A data structure is a way of organizing and storing data so that it can be accessed and used efficiently.

Data structures help to:
store large biological data
search and modify information
represent real-world relationships

| Data Structure | Type                                 | Why it is a data structure                  |
| -------------- | ------------------------             | ------------------------------------------- |
| **List** []    | Ordered, mutable collection of items | Stores multiple items in sequence           |
| **Tuple** ()   | Ordered, immutable                   | Stores multiple items but cannot be changed |
| **Dictionary {}| Key–value mapping                    | Stores data in pairs (fast lookup)          |
| **Set**    {}  | Unordered, unique values             | Stores unique elements only                 |

"""
s = {1,2,2,3}
print(s)
#this is set , output is only 1 ,2 3 it removes duplicates only unique values

"""
data coercion 
tuple([1,2,])
list((1,2,3)
converting a string into a list 
list("1","2","3")
list("abc)  #["a","b","c"]

| Function | Converts To | Example              |
| -------- | ----------- | -------------------- |
| str()    | string      | str(10) → "10"       |
| int()    | integer     | int("5") → 5         |
| float()  | float       | float("3") → 3.0     |
| list()   | list        | list((1,2)) → [1,2]  |
| tuple()  | tuple       | tuple([1,2]) → (1,2) |
| set()    | set         | set([1,1,2]) → {1,2} |
| dict()   | dictionary  | dict([(1,'a')])      |


| Feature    | List    | Tuple   | Set         | Dictionary  |
| ---------- | ------- | ------- | ----------- | ----------- |
| Ordered    | Yes     | Yes     | No          | No          |
| Mutable    | Yes     | No      | Yes         | Yes         |
| Duplicates | Allowed | Allowed | Not allowed | Keys unique |
| Indexing   | Yes     | Yes     | No          | By key      |
| Speed      | Normal  | Fast    | Fast        | Very fast   |

"""
print(True+1)


