"""
A bit = 0 or 1 (binary)
8 bits = 1 byte
01000001  → this 8-bit pattern is ONE BYTE
this number can be in different version and
each has some meaning a: number, a letter ,a symbol, raw file data

Byte = basic computer storage unit (8 bits)
bytes (Python) = raw binary data used for file-level operations, faster and encoding-free.

bytes are the smallest storage unit computers work with.
Every file in your system (FASTQ, BAM, image, PDF) is just a long sequence of bytes
"""

example=b"ATGC"
#This data is raw bytes, not text with language meaning.Each character becomes one byte.
#A is one byte (8 bits)
print(example)
print(example[0]) #65
#python shows the DECIMAL VALUE of those 8 bits of A
# for example , take this as one byte 01000001 convert into decimal version
"""

In Python, b"ATG" represents bytes. 
Each character is converted into one byte (8 bits) and stored in binary form.
Computers work with binary data, so bytes help the computer read and process files efficiently.
Since binary is not human-readable, Python shows the decimal value of each byte when accessed.
"""
#01000001 (binary) = 65 (decimal)

#b[0] returns the byte value NOT a character
#python decodes it , shows it in decimal version

#diff between string and bytes
s = "ATGC"
b = b"ATGC"
print(s[0])   # 'A'
print(b[0])   # 65
#string → human-readable text
#bytes → machine-readable numbers

#bytes are immutabel we can not change the A=65 , we can nut chnage the byte value
#Bytes map directly to memory,Changing them can corrupt files So Python protects them

"""
why we convert strings to bytes:
writing to binary file
sending data to tools
storing efficiently
avoiding encoding problems

why bytes are needed
Case 1: Reading files from disk ,Files on disk are always bytes, never strings.
Case 2: Compressed bioinformatics files ,Compressed data is pure binary.
Case 3: Performance (speed)Bytes: smaller ,faster,no encoding checks
That’s why: BAM files use bytes ,Not text
Case 4: Network / tools / pipelinesWhen Python talks to:HISAT2 ,BLAST ,samtools ,Linux commands
It sends bytes, not strings.
"""
#bytearray is the mutable version of bytes.
#It is used when we need to modify binary data, which is not possible with bytes.
example=bytearray(b"ATGCATG")
print(example)
print(example[1]) #84 , i can change that  to whatever i want
example[1]=12
print(example[1])

#if we want to assign new character , in the above we changed the value of that position ,
# but if we want to replace a with g
#we have to use ord() , means ordinal ,
# which convert that g which is string into ascii number , which is machine readable
dna = bytearray(b"ATGC")
print(dna)
dna[0] = ord('G')
print(dna)

