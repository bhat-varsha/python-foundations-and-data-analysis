"""
SeqIO is the input/output module in Biopython used to:
Read biological sequence files
Write biological sequence files

SeqIO always works with SeqRecord objects
Input → SeqRecord and  Output → SeqRecord

"""
#readind a file which has many sequence
from Bio import SeqIO
for record in SeqIO.parse("seqdump.txt","fasta"): #here fasta is seqrecord
    #File format is NOT auto-detected :You must specify format explicitly("fasta","genbank"
    print(record.id)
    print(record.seq)

#reading a single sequence file
from Bio import SeqIO
value=SeqIO.read("single_seq.txt","fasta")
print("single sequence")
print(value.id)
print(value.seq)
#SeqIO.read() throws an error if: File has 0 sequences ,File has >1 sequence


#Writing sequences to a FASTA file
from Bio import SeqIO
SeqIO.write(value, "output.fasta", "fasta")

#Or for multiple records:
#SeqIO.write(records_list, "output.fasta", "fasta")
