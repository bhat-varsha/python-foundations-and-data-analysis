"""
personally hated data type , idk why
==================================================
PYTHON DICTIONARIES – COMPLETE NOTES & EXAMPLES
==================================================

A dictionary stores data in key : value pairs.

Key Features:
• Stored as key-value pairs
• Keys must be unique
• Mutable (can be changed)
• Fast lookup
• Ordered (Python 3.7+ keeps insertion order)

Syntax:
dictionary_name = {key1: value1, key2: value2}

--------------------------------------------------
Bioinformatics Uses:
• Gene ID → Gene name mapping
• Codon → Amino acid table
• Sample ID → Expression value
• Mutation position → Mutation type
==================================================
"""

# ==================================================
# 1. CREATING A DICTIONARY
# ==================================================

gene = {
    "name": "BRCA1",
    "length": 1863,
    "type": "tumor suppressor"
}

print("Full Dictionary:", gene)
print("Access value using key:", gene["name"])


# ==================================================
# 2. ACCESSING VALUES
# ==================================================

print("Gene length:", gene["length"])

# Safer access using get()
print("Using get():", gene.get("type"))
print("Non-existing key:", gene.get("location"))  # Returns None


# ==================================================
# 3. ADDING & UPDATING VALUES
# ==================================================

# Add new key
gene["chromosome"] = 17
print("After adding chromosome:", gene)

# Update value
gene["length"] = 2000
print("After updating length:", gene)

# Using update()
gene.update({"type": "DNA repair gene"})
print("After update():", gene)


# ==================================================
# 4. DELETING VALUES
# ==================================================

# Delete using del
del gene["chromosome"]
print("After deleting chromosome:", gene)

# pop() removes and returns value
removed_value = gene.pop("length")
print("Removed value:", removed_value)
print("After pop():", gene)


# ==================================================
# 5. DICTIONARY METHODS
# ==================================================

print("Keys:", gene.keys())
print("Values:", gene.values())
print("Items:", gene.items())
print("Length of dictionary:", len(gene))


# ==================================================
# 6. LOOPING THROUGH DICTIONARY
# ==================================================

for key in gene:
    print("Key:", key, "Value:", gene[key])

print("\nUsing items():")
for key, value in gene.items():
    print(key, "→", value)


# ==================================================
# 7. NESTED DICTIONARY
# ==================================================

nested_gene = {
    "BRCA1": {
        "length": 1863,
        "organism": "Homo sapiens"
    }
}

print("Nested access:", nested_gene["BRCA1"]["organism"])


# ==================================================
# 8. CHECKING KEY EXISTENCE
# ==================================================

print("Is 'name' in gene?", "name" in gene)
print("Is 'location' in gene?", "location" in gene)


# ==================================================
# 9. CLEARING DICTIONARY
# ==================================================

temp_dict = {"a": 1, "b": 2}
temp_dict.clear()
print("After clear():", temp_dict)


# ==================================================
# IMPORTANT SUMMARY
# ==================================================

"""
Dictionary:
• Mutable
• Keys must be unique
• Fast searching
• Can store mixed data types
• Supports nesting
"""