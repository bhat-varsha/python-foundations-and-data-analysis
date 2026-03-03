#fucntional programming  tools in pyhton:lambda, map, filter, reduce
#Think of these as helpers to work with lists without writing long loops.

#1.lambda function : lambda is a small, one-line function without a name.
#used in the place of def function , when defining a small fucntion(Function is short) ,or fucntion Used only once
#Syntax :  variable = lambda arguments: expression

#Normal function
def square(x):
    return x * x
#same thing using lambda
square = lambda x: x * x
print(square(2))
#No def, No return ,One line only

#Example
add =     lambda a,b:              a + b
#variable=lambda aruguemntes(a,b):expression
print(add(2, 3)) #5

##############################################################################
#2.map() – Apply function to ALL items in a list,
#Syntax : map(function, iterable)

#normal way
nums=[1,2,3]
result=[]
for x in nums:
    result.append(x*x)
print(result)

#using map
numbers=[1,2,3] #this is iterable
result=list(map(lambda x:x*x,numbers)) #map always returns a map object, so we convert to list().
#variables=map(fucntion,iterable)
outcome1=list(map(square,numbers))
print(result)
print(f"outcome1 is {outcome1}") #in this i idnt use lamba , the above where i defined def square ,
#that is used , in that we dont have to use the arguements

#map example using string
dna=["atg","taa"]
outcome=list(map(lambda x: x.upper(),dna))
print(outcome)
######################################################################
#3.filter() – Select items based on condition,filter() keeps only elements that satisfy a condition.
#syntax:filter(function,iterable)

#normal way
num=[1,2,3,4,5]
even=[]
for x in num:
    if x%2==0:
        even.append(x)
print(even)
#using filter
num1=[1,2,3,4,5]
even1=list(filter(lambda x:x%2==0,num1))
print(f"filter function usage={even1}")
#another bio related example
example=["AT","ATG","TAGG"]
codon=list(filter(lambda x:len(x)>2,example))
print(f"codon lenght more than 2 :{codon}")

###################################################################
#reduce() – Combine ALL values into ONE: reduce() reduces a list to a single value.
#Not built-in → need to import it.
#suntax;reduce(function, iterable)

from functools import reduce #imported from functools

#normal way
num=[1,2,3]
total=0
for x in num:
    total+=x
print(total)
#using reduce
num1=[1,2,3]
sum=(reduce(lambda a,b:a+b,num1))
sum1=reduce(lambda a, b: a * b, [1, 2, 3, 4])
#variable=reduce(fucntion,iterable/sequence)
print(f"using reduce function {sum}")

"""
| Tool   | Purpose         | Output       |
| ------ | --------------- | ------------ |
| lambda | small function  | function     |
| map    | apply function  | list         |
| filter | select elements | list         |
| reduce | combine all     | single value |

🟢 Use List Comprehension when: ,You want a list ,Logic is simple ,Readability matters

🟡 Use map/filter when: You already have a function ,Writing functional-style code ,Required by assignment/interview

🔴 Use reduce when: Output is ONE value ,Combining elements step-by-step

#if u leanrt list comprehension , there is no need of all these map filter reduce 
#but u can use that 
"""
#map=apply function to all means (x*x like that function )
#filter=selecting element from list (means even odd max ,min)
#reduce=all that in one step(sum etc)



