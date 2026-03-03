from Bio import SeqIO, Entrez
from Bio.SeqUtils import gc_fraction
# -----------------------------
# PART 1: Working with text
# -----------------------------
print("=== Working with Text ===")
with open("text_input.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        print(line)

print("\n")

# -----------------------------
# PART 2: FASTA parsing (length + GC%)
# -----------------------------
print("=== FASTA Parsing ===")
input_fasta = "input.fasta"
for record in SeqIO.parse(input_fasta, "fasta"):
    print("ID:", record.id)
    print("Description:", record.description)
    print("Length:", len(record.seq))
    gc = gc_fraction(record.seq) * 100
    print("GC%:", round(gc, 2))
    print("-" * 40)

print("\n")

# -----------------------------
# PART 3: NCBI retrieval + GenBank parsing
# -----------------------------
print("=== NCBI Retrieval + GenBank Parsing ===")
Entrez.email = "varshbhat08@gmail.com"
acc_id = "NP_001191615.1"
handle = Entrez.efetch(db="protein", id=acc_id, rettype="gb", retmode="text")
gb_text = handle.read()
handle.close()
with open("input.gbk", "w") as f:
    f.write(gb_text)
for record in SeqIO.parse("input.gbk", "genbank"):
    print("Record ID:", record.id)
    print("Protein Sequence:")
    print(record.seq)
    print("Protein Length:", len(record.seq))
