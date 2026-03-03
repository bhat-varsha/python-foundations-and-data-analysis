import pandas as pd
#Pandas is a Python library for fast, easy data_analysis using labeled tabular data.
#Pandas Series is a 1-dimensional labeled array (like a single column).
#Syntax
#pd.Series(data)
"""Data analysis

Handling tables (like Excel)

Working with CSV files

Handling missing data

Label-based indexing"""

s = pd.Series([10, 20, 30])
print(s)

#Pandas DataFrame is a 2-dimensional table with rows and columns.
#Syntax
#pd.DataFrame(data)

df = pd.DataFrame({
    "Gene": ["A", "B", "C"],
    "Expression": [12.5, 15.2, 13.8]
})
print(df)
df["label"] = ["high", "low", "low"] # Add column
print(df)
print(df["label"]) #print a column  , column selection
print(df.loc[0])  #row selection
print(df.iloc[0]) #row selection
print(df.info()) # Summary of the dataframe
print(df.describe()) # statistical summary of the numerical column(gives mean mix min
print(df.tail()) #shows last 5 rows
print(df.head()) #shows top 5 rows
print(df["Expression"]>200) # shows true and false
print(df[df["Expression"]>200])#Filter and shows the record
print(df.isnull()) # if value is None
print(df.fillna(500))  #Handling missing value
df = df.rename(columns={"gene": "geneName"}) #rename the column
print(df)
#_____________________________________________________________________________________________
#2
#Importing Files
df = pd.read_csv("data.csv")
df1 = pd.read_excel("data.xlsx")
df2 = pd.read_csv("data.txt", delimiter="\t")

#Exporting Files
df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)
df.to_csv("output.txt", sep="\t", index=False)

#Pandas vs NumPy
"""
NumPy	            Pandas
Numerical arrays	Labeled tabular data
Fast math	        Data analysis
No column names	    Column names
"""
#Bioinformatics exam mini-example
df = pd.read_csv("genes.csv")
high_exp = df[df["Expression"] > 10]
print(high_exp)

#_____________________________________________________________________________________________________
#Data Wrangling means cleaning, selecting, transforming, and summarizing data so it can be analyzed.

df = pd.DataFrame({
    "Gene": ["A", "B", "C"],
    "Expression": [12.5, 15.2, 13.8]
})
#Filtering , Selecting rows that satisfy a condition.
#SYNTAX: df[condition]
print(df[df["Expression"] > 10])

#Grouping (groupby) Dividing data into groups based on a column.
#Syntax : df.groupby("column")
print(df.groupby("GeneType"))

#Aggregation ,Applying summary functions to groups (mean, sum, count, max).
df.groupby("GeneType")["Expression"].mean()
#groupby = split data
#aggregation = summarize data

#Reshaping Changing the structure/layout of data (rows ↔ columns).
df = pd.DataFrame({
    "Gene": ["A", "A", "B", "B"],
    "Sample": ["S1", "S2", "S1", "S2"],
    "Expression": [10, 15, 8, 12]
})
#Pivot,rows ↔ columns,converts unique values into rows and columns.
#df.pivot(index=..., columns=..., values=...)
df.pivot(index="Gene", columns="Sample", values="Expression")
#index	    What becomes ROW names
#columns	What becomes COLUMN names
#values	    What fills the table
#Pivot is used to convert long-format biological data into matrix format.

#Melt,opposite of pivot,converts wide data → long data
#syntax;pd.melt(df, id_vars=[...])
pd.melt(df, id_vars=["Gene"]) #Keep Gene fixed, melt all other columns.
#id_vars = columns you want to KEEP AS IDENTIFIERS

#Bioinformatics-style mini example (exam perfect)
import pandas as pd
df = pd.DataFrame({
    "Gene": ["A", "A", "B", "B"],
    "Sample": ["S1", "S2", "S1", "S2"],
    "Expression": [10, 15, 8, 12]
})
result = df.groupby("Gene")["Expression"].mean()
print(result)
