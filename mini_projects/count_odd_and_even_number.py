numbers=list(map(int,input("enter the numbers using comma:   ").split(",")))
"""here we can use spaces also for that we use only split()
split will converst the input into separetae strings 
and map(int, will go into the input convert each number into integer 
if we dont use map it does not go to each evry number 
and list function is to convert that map object into list 
map object is not human readable"""
odd_count=0
even_count=0

for n in numbers:
    if n %2==0:
        even_count+=1
    else:
        odd_count+=1
print(f'even count is {even_count} and odd_count is {odd_count}')

#or else we can use for loop also
example=[int(n) for n in input("enter tne number using spaces").split() ]
# here i used spaces so i used only split and split have to write besing the bracket of input only
#because the function input has to work then map and int
odd=0
even=0
for number in example:
    if number %2==0:
        even+=1
    else:
        odd+=1
print("odd_count is =",odd)
print("even count is =",even)
