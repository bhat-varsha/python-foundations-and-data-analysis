#POLYMORPHISM :Polymorphism means “one thing, many forms”.
# In OOP, it refers to the ability of the same method/function name to behave differently for different objects.
#sound() in Animal → different for Dog and Cat
#USES
#same code works for different objects
#reduces code duplication
#makes program flexible

class Sequence:
    def __init__(self, seq):
        self.seq = seq
    def info(self):
        return "Generic sequence"
class DNASequence(Sequence):
    def info(self):  # polymorphism (overriding)
        return "DNA sequence"
class RNASequence(Sequence):
    def info(self):
        return "RNA sequence"
s1 = DNASequence("ATGC")
s2 = RNASequence("AUGC")
print(s1.info())
print(s2.info())
