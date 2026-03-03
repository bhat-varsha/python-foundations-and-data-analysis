"""
Biopython = library
Bio = main package inside the Biopython library
Inside Bio, there are modules (files):Bio
                                         ├── Seq.py
                                         ├── SeqRecord.py
                                         ├── SeqIO.py
                                         ├── AlignIO.py
                                         ├── PDB
Inside modules, there are classes
| Module          | Class inside            |
| --------------- | ----------------------- |
| `Bio.Seq`       | `Seq`, `MutableSeq`     |
| `Bio.SeqRecord` | `SeqRecord`             |
| `Bio.SeqIO`     | functions to read/write |


Biopython is a Python library specifically created for computational biology and bioinformatics.
Biopython is an open-source collection of Python tools designed for computational biology and bioinformatics,
enabling efficient handling of biological sequences, structures, databases, and analysis workflows.
It is a wrapper / interface
It helps you:Run tools,Parse outputs,Automate analysis
biopython is a library (collection of modules)
module is a python file which has functions where it is defined
| class         | Purpose                     |
| ------------- | --------------------------- |
| `Seq`         | Handle biological sequences |
| `SeqRecord`   | Sequence + metadata         |
| `SeqIO`       | Read/write sequence files   |
| `AlignIO`     | Read/write alignment files  |
| `Entrez`      | Access NCBI                 |
| `Blast`       | BLAST results handling      |
| `PDB`         | Protein structures          |
| `Restriction` | Restriction enzyme analysis |


pip install biopython (to install this in terminal)

Core modules /class (as per outline)
Seq
MutableSeq
SeqRecord
SeqIO
AlignIO

Additional modules
Alphabet
SeqUtils
Restriction
SwissProt
Prosite
PDB
\\
What is Biopython?

Biopython is a Python library (package) made specially for bioinformatics / computational biology.

It provides ready-made tools to handle and analyze biological data like:
DNA / RNA / Protein sequences
FASTA, GenBank, FASTQ files
Alignments
Phylogenetic trees
Biological databases (NCBI etc.)

So instead of writing everything from scratch, we use Biopython.

How Biopython is useful in Biological Science?

Biopython helps in biological science by making data_analysis faster and easier.
1) Sequence file handling (most common use)
Read/write files:
FASTA
FASTQ
GenBank
2) Sequence operations
You can easily perform:
complement / reverse complement
transcription (DNA → RNA)
translation (RNA → Protein)
✅ Using Seq
3) Database access (NCBI)
Biopython provides tools like:
Entrez to fetch sequences from NCBI
This is useful in:
gene study
genome research
molecular biology projects
4) Sequence alignment and phylogeny
Biopython supports:
pairwise alignment
multiple sequence alignment
phylogenetic tree creation/handling
5) Protein structure analysis
Using Bio.PDB, you can:
read PDB files
analyze chains, residues
extract sequences from structures

Useful in:
structural biology
drug design
"""


