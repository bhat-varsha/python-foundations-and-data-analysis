A = open("brucella_melitensis.fasta","r")
file_contents = A.read()
print(file_contents)
A.close()
SeqCount = open("brucella_melitensis.fasta", "r")
n = 0
for line in SeqCount:
    if line.startswith("@"):
        n = n+1
print(n)
SeqCount.close()

with open("Brucella_Out.fasta","r") as fi:
    for line in fi:
        if line.startswith(">"):
            print(line.strip())
        else:
            print(len(line))


# Extract Header from fasta sequence file
with open("brucella_melitensis.fasta") as brucella_input, open("Brucella_Out.fasta","w") as brucella_output:
    for line in brucella_input:
        if line.startswith(">"):
            brucella_output.write(line)
#__________________________________________________________________________________________
from Bio import AlignIO
alignment = AlignIO.read(open("TEM_SHV.fas"), "fasta")
print("Number of sequences:", len(alignment))
print("Alignment Length", alignment.get_alignment_length())
for record in alignment:
    print(record.id)
    print(str(record.seq))
    gap_count = record.seq.count("-")
    print(record.id, "Gaps:", gap_count)
# For conseved Sequence Identification
for i in range(alignment.get_alignment_length()):
    column = alignment[:, i]
    if len(set(column)) == 1:
        print("Conserved position", i+1, ":", column[0])
#__________________________________________________________________________________________--
# Find the complete restriction enzymes along with their recognition sites
from Bio.Restriction import AllEnzymes
enzymes = AllEnzymes
enzyme_sites = {}
for enzyme in enzymes:
    enzyme_name = enzyme.__name__
    recognition_site = enzyme.site  # Convert the site sequence to a string
    enzyme_sites[enzyme_name] = recognition_site
for name, site in enzyme_sites.items():
    print(f"{name:<30}{site}")


# Restriction Enzymes
from Bio.Seq import Seq
from Bio.Restriction import RestrictionBatch  # Work with a group of restriction enzymes
sequence = Seq("GAATTCGCGGCCGCTTAAGCTT") # Define a DNA seq
# EcoRI,NotI,and HindIII recognizes the site GAATTC, GCGGCCGC, AAGCTT respectively.
enzymes = RestrictionBatch(["EcoRI","NotI","HindIII"])
print(enzymes.search(sequence))
#__________________________________________________________________________________________-
from collections import Counter
from Bio.Seq import Seq
seq = Seq("ATGCGTA")
print(Counter(seq))

from Bio.SeqUtils import GC
from Bio.Seq import Seq
from Bio.SeqUtils import molecular_weight
seq = Seq("ATGCGCGTA")
print("GC Contents", GC(seq))
print("Molecular Weight:", molecular_weight(seq, "DNA"))

#from Bio.SeqUtils import GC123
from Bio.SeqUtils import GC
from Bio import SeqIO
with open("Brucella_Out1.fasta") as InputFile:
    for i in SeqIO.parse(InputFile, "fasta"):
        print(GC(i.seq))

#_____________________________________________________________________________________
from Bio.Seq import Seq
seq = Seq("ATGCGATACGCTTACGATCG")
motif = "TCG"
location = seq.find(motif)
print("First Location:", location)


from Bio.Seq import Seq
seq = Seq("ATGCGATACGCTTACGATCG")
motif = "A"
positions = []
for i in range(len(seq) - len(motif) + 1):
    if seq[i:i+len(motif)] == motif:
        positions.append(i)
print("Motif found at positions:", positions)


from Bio import SeqIO
motif = "ATG"
for i in SeqIO.parse("Brucella_Out1.fasta", "fasta"):
    if motif in i.seq:
        location = i.seq.find(motif)
        print(i.id, "contains motif at:", location)

#__________________________________________________________________________________________
