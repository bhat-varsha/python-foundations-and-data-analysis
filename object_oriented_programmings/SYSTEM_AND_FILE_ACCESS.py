"""
What is System access? ,
System access means Python can interact with the operating system (OS) to do tasks like:
run commands
check environment variables
get current directory
manage processes

What is File system access? ,File system access means Python can:
create/delete files & folders
list directories
rename/move files
check if file exists
get paths

Persistent Storage (MAIN idea) Persistent storage means saving data permanently so that it remains even after:
program ends
system restarts
"""
#System Access in Python (os, subprocess)
#Get current directory
import os
print(os.getcwd())
#Change directory
os.chdir("C:/Users/Varsha/Documents")
#to get the list of files
import subprocess
subprocess.run(["ls"])
subprocess.run(["fastqc", "sample.fastq"])

#File System Access (os, pathlib, shutil)
#Make / remove folder
os.mkdir("results")
os.rmdir("results")
#Copy / move files (shutil)
import shutil
shutil.copy("seqdump.txt", "backup.txt")
shutil.move("backup.txt", "folder/backup.txt")

#Persistent Storage Methods (EXAM)
#Method 1: Store in Normal Files
with open("output.txt", "w") as f:
    f.write("GC Content = 52%\n")
#Method 2: CSV storage (structured)
import csv
with open("result.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["SeqID", "Length"])
    writer.writerow(["seq1", 120])

