"""
In real datasets, a sequence always comes with:
An ID ,A name ,A description ,Annotations ,Database references

| Attribute     | Meaning                 |
| ------------- | ----------------------- |
| `seq`         | Sequence (`Seq` object) |
| `id`          | Primary identifier      |
| `name`        | Short name              |
| `description` | Full description        |
| `annotations` | Dictionary of metadata  |
| `features`    | Biological features     |
| `dbxrefs`     | Database references     |


Seq stores only the sequence.
SeqRecord stores sequence + metadata.

SeqIO works only with SeqRecord
Alignments are collections of SeqRecord
"""
#Seq → to store the sequence
#SeqRecord → to store sequence + information
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
# Create a sequence
dna_seq = Seq("ATGTGCGTACAT")
# Create SeqRecord with metadata
record = SeqRecord(
    dna_seq,
    id="Seq001",
    name="Human_DNA",
    description="Sample DNA sequence"
)
# Add annotation
record.annotations["organism"] = "Homo sapiens"
print(record.id)
print(record.name)
print(record.description)
print(record.seq)
print(record.annotations)
"""
You usually do NOT create SeqRecord manually
When you read a file:
from Bio import SeqIO
record = SeqIO.read("example.fasta", "fasta")

Biopython automatically creates a SeqRecord for you.
So:
FASTA → SeqRecord
GenBank → SeqRecord
EMBL → SeqRecord
"""