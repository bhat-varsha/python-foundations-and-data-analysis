#AlignIO is the Biopython module used to read and write sequence alignment files.
#These are multiple sequence alignments (MSA), not single sequences

#A single sequence → SeqRecord
#Multiple aligned sequences → Alignment object
#ALIGNIO DOES NOT ALLIGN TWO SEQUENCE IT READS ALLIGNED SEQUENCES
#to find how many gaps are there in alligned sequence , and lenght of seq after and befroe allignment

"""
AlignIO is a Biopython module used to read and write sequence alignment files.
AlignIO is the input/output module in Biopython used to read and write
multiple sequence alignments in standard alignment formats.

In bioinformatics, we often work with aligned sequences, such as:
Multiple Sequence Alignments (MSA)
Phylogenetic analysis
Conserved region identification

AlignIO helps to:
read alignment files
store them in alignment objects
write alignments to output files

3. Important Points about AlignIO (Very Important for Exams)
AlignIO works with alignment files, not raw sequences
Input → MultipleSeqAlignment object
Each alignment contains multiple SeqRecord objects
File format must be specified explicitly

SeqIO → SeqRecord
AlignIO → MultipleSeqAlignment

5. Reading an Alignment File (AlignIO.read)

Used when the file contains only one alignment.

Syntax
from Bio import AlignIO
alignment = AlignIO.read("file.aln", "clustal")

6. Writing an Alignment File

Used to write alignment data into a file.
AlignIO.write(alignment, "output.aln", "clustal")

7. Accessing Alignment Data
print(alignment)
print(len(alignment))          # number of sequences
print(alignment.get_alignment_length())

"""
from Bio import AlignIO
# Read alignment file
alignment = AlignIO.read("sample.aln", "clustal")
# Print alignment
print(alignment)
# Number of sequences
print("Number of sequences:", len(alignment))
# Length of alignment
print("Alignment length:", alignment.get_alignment_length())
# Print each sequence ID and sequence
for record in alignment:
    print(record.id)
    print(record.seq)

#Bio.Align is used to create and perform sequence alignments.
from Bio.Align import PairwiseAligner
seq1 = "ATGCT"
seq2 = "ATGTT"
aligner = PairwiseAligner()
alignments = aligner.align(seq1, seq2)
print(alignments[0])
print("Score:", alignments[0].score)
"""
8. Difference Between SeqIO and AlignIO (Short – Exam Favorite)
SeqIO	AlignIO
Works with sequences	Works with alignments
Returns SeqRecord	Returns MultipleSeqAlignment
For FASTA, GenBank	For aligned FASTA, CLUSTAL
Single sequences	Multiple aligned sequences

9. Where AlignIO is Used (Bioinformatics Aspect)
Multiple sequence alignment analysis
Conserved motif detection
Phylogenetic tree construction
Comparative genomics
"""
