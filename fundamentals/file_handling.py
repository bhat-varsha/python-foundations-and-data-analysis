"""
File handling is the process of: opening a file ,reading or writing data ,closing the file safely
In bioinformatics, data is huge, so files are used instead of variables.
types of biological files:
| File type | Purpose                   |
| --------- | ------------------------- |
| FASTA     | Stores sequences          |
| FASTQ     | Stores sequence + quality |
| SAM       | Alignment text file       |
| BAM       | Binary alignment file     |
| TXT       | Results / logs            |


| Mode   | Meaning            |
| ------ | ------------------ |
| `"r"`  | read               |
| `"w"`  | write (overwrites) |
| `"a"`  | append             |
| `"rb"` | read binary        |
| `"wb"` | write binary       |

"""

#to open file

#1 for small files
file=open("../core_python/core python/seqdump.txt", "r") #if we just write this it wont print anything
print(file)
#it does not give output becasue open fucntion is this only “I opened the door, but I didn’t look inside.
#open() does NOT read the file ,It only creates a file object (a connection)
content=file.read()  #.read go throgh the file
print(content)
file.close() #close functiin:file stays open in memory,memory leak,file lock issue ,problem opening another file

#2.to read a small line
file=open("../core_python/core python/line.txt", "r") # if i pasted the same big file , it will print only the first line of thst file
content=file.readline()
print(content)
file.close()

#3.looping through the files
files=open("../core_python/core python/seqdump.txt", "r")
for line in files:
    print(line.strip())
file.close()
#strip() :Removes \n (newline),Removes extra spaces, Makes output clear

#4.count how many seq in fasta file
#first we have to open that file
fasta_file=open("../core_python/core python/seqdump.txt", "r")
no_of_sequence=0
for sequence in fasta_file:
    if sequence.startswith(">"):
        no_of_sequence+=1
print(no_of_sequence)  #3
fasta_file.close()

with open("../core_python/core python/seqdump.txt", "r") as fasta_file:
    content = fasta_file.read()
    print(content.count(">"))



#5. with statement ,: here no need of closing the file
with open("../core_python/core python/line.txt", "r") as file:
    for line in file:
        line=line.strip()
        if line=="":
            continue
        print(line)
file.close()


#writing to a file by creating a new file
with open("../core_python/core python/line1.txt", "w") as file_output:
    file_output.write("this is new line in new file")
#writing in a file with alread exsist file :without erasing the alread availabel line
with open("../core_python/core python/line.txt", "a") as file_output:
    file_output.write("this is new line in new file")
print(file_output)