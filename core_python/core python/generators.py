#generator function that:produces values one at a time ,instead of storing everything in memory
#Think of it like reading a file line-by-line, not loading the whole file.
#A generator is a Python function that yields values one at a time using yield,
# enabling memory-efficient iteration over large datasets.
#Imagine FASTQ file:10 million reads
#List approach:Read all 10 million into RAM ❌ crash
#Generator:Read one read,Process it,Forget it,Move on,Works efficiently

#Python creates the entire list first ,Stores [1,2,3,4] fully in memory ,Returns it
def get_numbers():
    return [1,2,3,4,5]
print(get_numbers())
#we can access by
number=get_numbers()
print(number[0])
print(number[3])
#accessing elements one-by-one AFTER the full list is already created.
print("whole list one by one,down here")
for num in number:
    print(num)


def get_numbers_in_generator():
    for i in range(1,5):
        yield i
print(get_numbers_in_generator())#<generator object get_numbers_in_generator at 0x000001815B703510>
gen=get_numbers_in_generator()#here gen is a generator object which stores the value
#generator object is a paused function
print(next(gen))
#what next does :Start function ,Run until first yield ,Return value ,PAUSE function at that exact line
print(next(gen))
#yield pauses the function, saves its state, and resumes from there next time.
#Unlike return, yield does not stop the function permanently.
with open("file.txt") as f:
    for line in f:
        print(line)
#f is actually a generator-like object:It gives one line at a time ,Saves memory

