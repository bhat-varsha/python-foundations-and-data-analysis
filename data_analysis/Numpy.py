"""
Python Library? A Python library is a collection of pre-written code (modules and functions)
that helps programmers perform specific tasks easily without writing everything from scratch.

Why libraries are used
Save time and effort
Provide optimized and tested functions
Make programs shorter, readable, and efficient
Essential for scientific, data, and visualization work

NumPy : NumPy (Numerical Python) is a Python library used for numerical and mathematical computations,
especially with arrays and matrices.

Handles large numerical datasets efficiently
Faster than Python lists
Supports mathematical, statistical, and linear algebra operations
Backbone for many other libraries (Pandas, SciPy, ML libraries)

Function	Purpose
np.array()	Create an array
np.zeros()	Array of zeros
np.ones()	Array of ones
np.arange()	Range of values
np.mean()	Mean
np.sum()	Sum
np.max()	Maximum
np.min()	Minimum
np.reshape()	Change shape
np.dot()	Matrix multiplication
np.linspace()	Evenly spaced values
ndim	Number of dimensions
shape	Rows & columns
dtype	Data type
#bulit in function with mean min max
np.std()	Standard deviation
np.sqrt()	Square root
np.exp()	Exponential
np.log()	Logarithm
"""
#__________________________________________________________________________________________________________--
#1 numpy array
#A NumPy array is a homogeneous, fixed-size, multidimensional data structure used to store numerical data.
#syntax
import numpy as np
#array_name = np.array(iterable)

import numpy as np
print("I am using the version of libraries:", np.__version__)
#numpy=Fast, mathematical container for numbers
#numerical python
#the diff between list and numpy
my_array = np.array([1,2,3,4,5]) #convert list to np.array
print(my_array*2) #2 multiply with all elements
list=[1,2,3,4,5]
print(list*2) #but this repeat the whole list

# Create a NumPy array in to list
my_array = np.array(list) #np.array converts list into array
print("array:",my_array)
print("type:",type(my_array))
#conver array to list , .tolist the code
python_list = my_array.tolist()  # convert array to list
print("Python List:", python_list)
print("Type:", type(python_list))

a = np.array([[1,2,3], [4,5,6]]) #2D array
print("Array a:", a)
print("Shape:", a.shape) #rows and columns (2,3)
print("Size:", a.size) #6 (2*3)
print("Data type:", a.dtype) #int64
print(a.reshape(3,2)) #change the shape of an array , 2 row 3 three column to vice versa
print(a.ndim) #dimension like one d or 2 d like that
print(a.T) # Transpose the arrayy
#same as reshape but it completely reshare the array like row to column and vice verse

x=np.arange(12) #from 0 to 12 , i will arange like range function in numpy we use arange
print(x)
x=np.arange(0,10,2)
print(x)
z = np.zeros((3,4)) #full zero of 3 row and 4 column
print(z)
x = np.ones((2,3)) #same for one
print(x)
y = np.eye(8)  #identity matrix # along the intersection poits only one , that for 8 by 8
print(y)
w= np.linspace(0,1,5) #the value between 0 and 1 that is divided into 5 equal parts
print(w)

print(np.mean(my_array)) #1d
print(np.mean(a,axis=0)) #2D , for this 0 column , 1=row
#same for all numerical operations
#_________________________________________________________________________________________--
#2.
#Numerical Operations on NumPy Arrays
#numerical operations in NumPy are element-wise operations performed directly on arrays without loops.
"""Syntax
array1 operator array2
"""
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division
#Scalar Operations
a = np.array([1, 2, 3])
print(a * 2) #[2 4 6]
#can apply mean sum etc
h = np.array([1, 2, 3])
i = np.array([4, 5, 6])
j = h + i
print("j=", j)

#__________________________________________________________________________________________________
#3.
#Array Slicing , Array slicing means extracting a portion of an array using index ranges.
#Syntax
#array[start : stop : step]

#1D slicing
arr = np.array([10, 20, 30, 40, 50])
print(arr[1:4]) #[20 30 40]
print(arr[::2]) #[10 30 50] # print every second elements
print(arr[::-1]) #Reverse an array

#2D Array Slicing
#array[row_start:row_end , col_start:col_end]

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print(arr[0:2, 1:3]) #[[2 3]
                    #[5 6]]
print(arr[0,2])  #when u want only one number
print(arr[0:2,0:2])

#Slicing returns a view, not a copy
#Changes in sliced array affect original array
#Copy vs View
slice_arr = arr[0:2, 0:2].copy()
print(slice_arr)
#NumPy slicing returns a view, not a copy.
#Use .copy() to create an independent array.

#___________________________________________________________________________________________
#4
#Broadcasting
# Broadcasting is a NumPy mechanism that allows arrays of different shapes to perform element-wise operations.
#Broadcasting Rules
    #Arrays must have compatible shapes
    #Dimensions are compared from right to left
#Dimension is compatible if: They are equal , One of them is 1

#(Scalar Broadcasting)
arr = np.array([1, 2, 3])
print(arr + 10) #[11 12 13]

#(Array Broadcasting)
a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([10, 20, 30])
print(a + b)  #[[11 22 33]
                #[14 25 36]]

#When Broadcasting FAILS
a = np.array([1, 2, 3])
b = np.array([1, 2])
# a + b → ERROR (shapes not compatible)

#_____________________________________________________________________________________________
#5.
#Expressions & Logical Operations (NumPy way)
x = 10
print(x > 5 and x < 20)

arr = np.array([5, 10, 15, 20, 25])
print(arr[(arr > 10) & (arr < 25)])
"""
and	&
or	`
not	~
"""
#Boolean Indexing
arr = np.array([10, 20, 30, 40])
print(arr>10) #false true true true
print(arr[arr > 20]) # 30 ,40

#Arrays → Efficient numerical storage
#Array slicing → Extract parts of arrays
#Broadcasting → Operations on different-shaped arrays
#numPy avoids loops → faster & cleaner code


#Calculate GC content of a DNA sequence using NumPy.
import numpy as np
dna = "ATGCGGCTTAACG"
dna_array = np.array(list(dna))
gc_count = np.sum((dna_array == 'G') | (dna_array == 'C'))
gc_content = (gc_count / dna_array.size) * 100
print(gc_content)

#Optional second example (one-liner for viva)
# Calculate mean gene expression value
expression = np.array([12.5, 15.2, 13.8, 14.9])
print(np.mean(expression))

#______________________________________________________________________________________
#Sorting ,Sorting means arranging elements in ascending or descending order.
#syntax= np.sort(array)
arr = np.array([30, 10, 20, 50])
print(np.sort(arr)) #[10 20 30 50]
#Sorts row-wise by default

#Searching ,Searching means finding index positions of elements.
#argmax() – index of maximum value
arr = np.array([10, 50, 20])
print(np.argmax(arr)) #1

#argmin() – index of minimum value
print(np.argmin(arr)) #0

#The random module is used to generate random numbers for simulations, testing, and modeling.

#rand() → random numbers between 0 and 1
np.random.rand(5) #split into 5 parts
#[0.23 0.76 0.54 0.11 0.89]

#randint() → random integers
np.random.randint(1, 10, 5)
#from 1 to 9 generate 5 numbers

#Fixing randomness
np.random.seed(42)

