"""
SeqUtils = Sequence Utilities (especially used for proteins)
It is a helper module in Biopython that provides:Basic biological calculations Derived properties from sequences

SeqUtils is mainly used for sequence analysis and derived biological properties.
SeqUtils works on Seq / string objects, not files directly.

It does not store sequences
It does not read files
It analyzes sequences you already have.

Inside SeqUtils, there are submodules:
Bio.SeqUtils
 ├── ProtParam
 ├── GC
 ├── CodonUsage
 └── molecular_weight
 SeqUtils is a Biopython utility module that provides tools for calculating biologically relevant properties of sequences.
The ProtParam submodule includes the ProteinAnalysis class,which is used to compute physicochemical properties of proteins
such as molecular weight, isoelectric point, amino acid composition, instability index, and hydrophobicity.
These properties are important for understanding protein behavior, stability, and function.
"""
from Bio.SeqUtils.ProtParam import ProteinAnalysis
protein_seq = "MKWVTFISLLFLFSSAYS"
analysis=ProteinAnalysis(protein_seq)
print(analysis.length)
print(analysis.molecular_weight()) #Mass of the protein (Daltons)
print(analysis.isoelectric_point()) #pH at which protein has zero net charge
print(analysis.instability_index())
print(analysis.amino_acids_percent)  #amino acid percentage
print(analysis.gravy())#hydrophobicity

#gc content
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
fasta_file = "input.fasta"
for record in SeqIO.parse(fasta_file, "fasta"):
    seq = record.seq
    gc_percent = gc_fraction(seq) * 100
    print("ID:", record.id)
    print("Length:", len(seq))
    print("GC%:", round(gc_percent, 2))