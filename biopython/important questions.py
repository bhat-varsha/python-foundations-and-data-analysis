#what is Seq and Seqrecord (difference ,example)
#A biological sequence object (DNA / RNA / Protein) with sequence operations.
#It is like a string, but with bioinformatics methods. ,reverse complement
# transcription ,translationm ,complement ,slicing like string
from Bio.Seq import Seq
dna = Seq("ATGCCGTA")
print(dna)
print(dna.complement())
print(dna.reverse_complement())
print(dna.transcribe())
print(dna.translate())

#Seq recorcdvA record that stores Seq + metadata (ID, name, description, annotations).
# It is used when reading from FASTA/GenBank using SeqIO.parse().
from Bio import SeqIO
record = next(SeqIO.parse("input.fasta", "fasta"))
print(record.id) #this four are seq reocrd ,
print(record.description)
print(record.seq)
print(len(record.seq))
"""
Feature	        Seq	                                        SeqRecord
Stores	        only sequence	                            sequence + metadata
Type	        sequence object	                            full biological record
Methods     	translate, complement, rev_comp	contains    seq + annotations
Used for	    sequence operations	                        file parsing / database records
"""
#✅ Seq = sequence only
#✅ SeqRecord = sequence + information about sequence (metadata)

#_______________________________________________________________________________________
#what is biopython , how it usefull in biological science pasted in basics
#purpose of seq io module , in seq io
#programm for printing id and lenght ,
#entrex all in codes in biopython
#sequtil in sequtils
#diff between seq and mutable seq'
#_________________________________________________________________________________________
#What is Alignment?
#Arranging two (or more) sequences to identify regions of similarity (matches),
# and differences (mismatches/gaps).

#Biopython Align module (definition

from Bio import AlignIO
alignment = AlignIO.read("alignment.aln", "clustal")
print(alignment)
print("Total sequences:", len(alignment))
print("Alignment length:", alignment.get_alignment_length())

