row=3
for i in range (1,row+1):
    print("*" * i)
i=1
while i<5:
    print("*" * i)
    i+=1

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

rows = int(input("Enter number of rows: "))

# Upper pyramid
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

# Lower inverted pyramid
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
