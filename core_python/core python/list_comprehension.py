"""
A list comprehension is a short and readable way to create a list from another iterable (list, string, range, etc.)
syntax:[expression for item in iterable]
"""
numbers = [1, 2, 3]
new_list = []
for x in numbers:
    new_list.append(x + 1)
print(new_list)

numbers = [1, 2, 3]
new_list = [x + 1 for x in numbers]  # List comprehension
print(new_list)

nums = [1, 2, 3, 4]
squares = [x*x for x in nums]
        #=[expression for item in iteration]
print(squares)

#the expression can be anything
length=[len(word) for word in ["gene","protein","dna"]]
print(length) #4,7,3

#1.list comprehension with if condition
num=[1,2,3]
even=[x for x in num if x%2==0]
print(even)
#or
odd=[x for x in range(10) if x %2!=0]
print(odd)
#or with multiple condition
var=[x for x in range(20) if x%2==0 if x>10]
print(var) #[12, 14, 16, 18]

#2. list comprehension with if and else :
#synatx:
#[expression_if_true if condition else expression_if_false for item in iterable]
result = ["even" if x % 2 == 0 else "odd" for x in range(5)]
        #[result if  condition else result for loop]
print(result)
maximum=["max" if x>5 else "min" for x in range(7)]
print(maximum)

#3. list comprehension with strings
dna="ATGC"
bases=[x for x in dna]
print(bases)