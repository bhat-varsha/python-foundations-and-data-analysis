"""
object is a bundle of related attributes(data) and methods(functions)(methods are actions that object can perform
            ex:phone which is a data, function is call
            , cup, book
            neea a class to create many  object
class:is a type of blueprint ,used to design the structure and layout of object
    to create a class we need constructor , which is __init__,it is a dunder method , which means double __
"""
#CLASS
#Without class (normal coding)
seq1 = "ATGC"
seq2 = "ATGCGG"
print(len(seq1))
print(len(seq2))

#This works. Now imagine you also want:GC content ,Reverse sequence ,Complement sequence
#You’ll write: gc_content(seq) ,reverse(seq),complement(seq)

#A class lets you create ONE custom data type that bundles data and related operations together.
"""Sequence
 ├── sequence
 ├── length()
 ├── gc_content()
 └── reverse()
 That bundle is a class.
"""

#definition :A class is a blueprint used to create objects that contain data and functions together.
#to CREATE a class (simplest form)
class Sequence: #I am defining a new type called Sequence
    pass

#Adding DATA to a class (attributes) :A class can define what data it will hold.

class Sequence:
    def __init__(self, seq): #Data is set automatically when created ,So class + __init__() = ready-made box
        self.seq = seq #self refers to the current item created from the class.

#without init() :You must manually assign values ,Repetitive work

#A class can contain: Attributes → variables, Methods → functions
class Example:
    data = 10        # attribute
    def show(self):  # method
        print("Hello")

"""
Without Class	        With Class
Many variables	        One structured unit
Functions scattered	    Functions inside class
Hard to scale	        Easy to extend
Messy	                Clean
"""
#Problem:You are working with DNA sequences and want:Length ,GC content

#Without class
seq = "ATGCGC"
print(len(seq))
print((seq.count("G") + seq.count("C")) / len(seq))
#works, but not organised.

#With class (ONLY CLASS + IDEA)
class DNASequence:
    def __init__(self, seq):
        self.seq = seq

    def length(self):
        return len(self.seq)

    def gc_content(self):
        return (self.seq.count("G") + self.seq.count("C")) / len(self.seq)



#class is a blueprint,creates a custom data type,groups data+related functions,It makes programs clean and scalable


""" 
Why class is needed
to group data + functions together
to create many similar objects easily
"""



