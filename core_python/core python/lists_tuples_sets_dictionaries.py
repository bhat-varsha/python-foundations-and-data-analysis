#Lists store multiple values, can grow/shrink, and allow modification. Most flexible structure in Python.
#Storing multiple sequences, alignment results, gene lists.
#Lists are mutable and widely used to store biological datasets.
examples=["aug","abc"]
examples.append("tac")
print(examples)
#appned , pop , reverse , sort,insert,find,index

#Tuples are like lists but immutable. Used when data should not change, improving safety and speed.
#Fixed records like chromosome coordinates.
#Tuples are immutable and used for fixed biological data.
gene_loc = ("chr1", 100, 500)
print(gene_loc[1])

#Sets store unique elements only and automatically remove duplicates.
#Finding unique genes, SNPs, protein IDs.
#Sets are unordered collections with no duplicate values.
genes = {"BRCA1", "TP53", "BRCA1"}
print(genes)

#Dictionaries store data as key–value pairs, allowing very fast lookup.
#Codon tables, gene annotations, ID mappings.
#Dictionaries are used for biological mappings and annotations.
codon = {"AUG": "M", "UUU": "F"}
print(codon["AUG"])



