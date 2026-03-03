#Inheritance is a feature of OOP in which a new class (child/derived)
# acquires the properties and methods of an existing class (parent/base).

#code reuse
#reduces duplication
#easy to extend old class

#Syntax
#           class ChildClass(ParentClass):
#           ...
class Animal:
    def sound(self):
        print("Animal sound")
class Dog(Animal):   # inheritance
    def sound(self):
        print("Bark")
d = Dog()
d.sound()

#class inhertience
#Creating a new class (child/derived class) from an existing class (parent/base class).
#So the child class can: reuse the parent’s variables + methods ,add new features ,
# modify (override) parent methods

#Syntax of Inheritance
class ParentClass:
    # parent methods
    pass
class ChildClass(ParentClass):
    # child methods
    pass

#Code Example
class Sequence:
    def __init__(self, seq):
        self.seq = seq.upper()
    def length(self):
        return len(self.seq)
    def count_base(self, base):
        return self.seq.count(base.upper())
class DNASequence(Sequence):   # Inherits Sequence
    def gc_content(self):
        g = self.count_base('G')
        c = self.count_base('C')
        return ((g + c) / self.length()) * 100
dna = DNASequence("ATGCGCGTAA")
print("Sequence:", dna.seq)
print("Length:", dna.length())
print("Count of A:", dna.count_base("A"))

"""
OOP organizes program using classes and objects
Class = blueprint/template
Object = instance of class
AttribuTes = variables inside object
Methods = functions inside class
Inheritance = child class acquires parent class properties
OOP helps in reuse, modularity, easy maintenance
"""