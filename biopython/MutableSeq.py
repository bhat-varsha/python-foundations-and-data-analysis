#MutableSeq is similar to Seq, but:
#Seq → immutable (cannot be changed)
#MutableSeq → mutable (can be modified)
from Bio.Seq import MutableSeq
dna=MutableSeq("ATGTGTCTGA")
print(dna)
dna[0]="C"
print(dna)
#we can do all the function we did in seq , additionaly we can alter the bases alao ,
#which is not supported in seq
print(dna.reverse_complement())

from Bio.Seq import Seq
print(Seq(dna))  #converted dna which was mutable to immutable

#When MutableSeq is used :Sequence editing , Simulations ,Preprocessing pipelines