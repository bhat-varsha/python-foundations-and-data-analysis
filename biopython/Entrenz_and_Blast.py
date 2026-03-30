"""
Entrez is an NCBI search and retrieval system used to access biological databases such as nucleotide, protein, and PubMed.
BLAST is used to compare a biological sequence against database sequences to find regions of similarity.
NCBIWWW is used to submit BLAST searches to NCBI servers online.
NCBIXML is used to parse BLAST results stored in XML format.
"""
#entrez example
from Bio import Entrez, SeqIO
Entrez.email = "student@example.com"
handle = Entrez.efetch(db="nucleotide",id="NM_001204686.1",rettype="fasta",retmode="text")
record = SeqIO.read(handle, "fasta")
handle.close()
print(record.id)
print(record.seq)

#blast example
from Bio.Blast import NCBIWWW, NCBIXML
from Bio import SeqIO
record = SeqIO.read("input.fasta", "fasta")
result_handle = NCBIWWW.qblast(program="blastn", database="nt",sequence=record.seq)
blast_record = NCBIXML.read(result_handle)
print("Query:", blast_record.query)
print("Top Hit:", blast_record.alignments[0].title)

