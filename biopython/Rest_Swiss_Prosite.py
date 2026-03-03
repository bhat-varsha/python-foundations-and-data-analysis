"""
1. Restriction (Restriction Enzymes)
The Restriction module in Biopython is used to analyze restriction enzyme cut sites in DNA sequences.
Find restriction enzyme recognition sites
Simulate restriction digestion of DNA
"""
from Bio.Seq import Seq
from Bio.Restriction import EcoRI
dna = Seq("GAATTCGCGGAATTC")
print(EcoRI.search(dna))
#Finds EcoRI cut sites in the DNA sequence.

"""
2. SwissProt
SwissProt is a manually curated protein sequence database with high-quality annotations.
In Biopython, SwissProt records can be parsed and analyzed.

Purpose
High-quality protein annotations
Functional and structural protein information
"""
from Bio import SwissProt
# Example: parsing SwissProt file (conceptual)
# record = SwissProt.read(open("sample.dat"))
"""
Prosite is a database of protein domains, families, and functional sites.
Biopython provides tools to parse Prosite patterns and records.

Purpose
Identify protein motifs
Detect functional domains
"""
from Bio.ExPASy import Prosite
# record = Prosite.read(open("prosite.dat"))
"""
Very Short Difference (Optional Exam Table)
Tool	            Used for
Restriction	        DNA cut site analysis
SwissProt	        Curated protein database
Prosite	            Protein motifs & domains

"""