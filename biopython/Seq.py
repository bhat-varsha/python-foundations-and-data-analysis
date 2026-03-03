#Seq represents a biological sequence object (DNA, RNA, or Protein).
#funtions:complement,translate,transcription ,reverse complement
#   Seq is a class in the Bio.Seq module used to represent biological sequences such as DNA, RNA, and proteins.
#Biopython is a big package , inside that Bio.Seq is a module it has Seq ,mutablseq etc as class
from Bio.Seq import Seq
dna=Seq("ATGCATGC") #inside Seq is just a string , we have to convert the string to sequence
#python cant do translate and other function to string , but can do to seq
#so as we conver str to int , like that we use Seq function here
#string does not have biological meaning
print(f'original_dna {dna}')
print(f'dna_complement:{dna.complement()}')
print(f"dna_reverse_complement: {dna.reverse_complement()}")
print(f"dna_transcribe: {dna.transcribe()}")
print(f"dna_tranlate:{dna.translate(to_stop=True)}")

#seq is immuatbale
#Biological sequences are often treated as fixed,Prevents accidental changes,Improves data safety

