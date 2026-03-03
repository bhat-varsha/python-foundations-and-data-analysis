#codon usage
from Bio.Seq import Seq
from Bio.SeqUtils import CodonUsage
dna = Seq("ATGGCCATGGCCATGAAA")
codon_table = CodonUsage.CodonsDict()
for i in range(0, len(dna) - 2, 3):
    codon = str(dna[i:i+3])
    codon_table[codon] += 1
print("Codon usage:")
for codon, count in codon_table.items():
    if count > 0:
        print(codon, ":", count)

#motif search
from Bio.Seq import Seq
dna = Seq("ATGCGATATCGATATCG")
motif = "ATAT"
for i in range(len(dna) - len(motif) + 1):
    if dna[i:i+len(motif)] == motif:
        print("Motif found at position:", i+1)
