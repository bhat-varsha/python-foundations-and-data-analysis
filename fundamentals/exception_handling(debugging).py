#EXCEPTION HANDLING : An exception is a runtime error that stops the program.
# Why handle exceptions? Prevent program crash ,Show meaningful message ,Handle unexpected input

#Basic try–except
try:
    x = int(input("Enter number: "))
    print(10 / x)
except:
    print("Error occurred")

#Specific exceptions (BEST PRACTICE)
try:
    x = int(input())
    print(10 / x)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")

#else with exception : Runs only if no error occurs
try:
    print(10 / 2)
except:
    print("Error")
else:
    print("Success")

#finally : Runs always (error or not)
try:
    file = open("data.txt")
except:
    print("File error")
finally:
    print("Done")

#Raising exceptions manually
age = -5
if age < 0:
    raise ValueError("Age cannot be negative")

#Bioinformatics example (real-life)
seq=["ATGCATGC"]
try:
    gc = (seq.count("G") + seq.count("C")) / len(seq)
except ZeroDivisionError:
    print("Empty sequence")



"""Common Types of Exceptions (Important)
Exception	        When it happens	            Example
ZeroDivisionError	divide by 0	                10/0
ValueError	        wrong datatype conversion	int("abc")
TypeError	        wrong type operation	    "a" + 2
IndexError	        invalid index	            a[10]
KeyError	        key not found	            d["x"]
FileNotFoundError	file missing	            open("x.txt")
"""
#ValueError
try:
    x = int(input("Enter integer: "))
    print(x)
except ValueError:
    print("Invalid input! Please enter only integer.")

#FileNotFoundError (bioinformatics related)
try:
    file = open("input.fasta", "r")
    print("File opened successfully")
    file.close()
except FileNotFoundError:
    print("Error: FASTA file not found!")

