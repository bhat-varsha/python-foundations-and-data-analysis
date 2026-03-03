#conuting the no of fasta sequence in fasta file , using header of fasta seq
#Using Biopython SeqIO.parse()
from Bio import SeqIO
count = 0
for record in SeqIO.parse("input.fasta", "fasta"):
    count += 1
print("Number of sequences:", count)

#Method 2 (Simple Python): Count headers (>)
count = 0
with open("input.fasta", "r") as file:
    for line in file:
        if line.startswith(">"):
            count += 1
print("Number of sequences:", count)
