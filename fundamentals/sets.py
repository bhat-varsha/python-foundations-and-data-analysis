"""
A set is an unordered collection of unique elements.
No duplicates
Mutable
Supports mathematical operations

finding unique mutations
comparing gene sets
intersection of pathways
"""
# Creating sets
set1 = {10, 20, 30, 40, 50}
set2 = {40, 50, 60, 70, 80}
print("Set 1:", set1)
print("Set 2:", set2)

#thses all functions can not be done in one line
set1.add(90) # Adding an element only single element
print("After add(90):", set1)


set1.update([100, 110]) # Updating with multiple elements,many at once
print("After update:", set1)

set1.remove(20) # Removing an element (throws error if not found)
print("After remove(20):", set1) # Discarding an element (no error if not found)
set1.discard(200)  # 200 not present, but no error
print("After discard(200):", set1)
#Pop a random element
removed = set1.pop()
print("After pop(), removed:", removed)
print("Set now:", set1)
# Clear the set
temp_set = {1, 2, 3}
temp_set.clear()
print("After clear():", temp_set)
# Set union
print("Union:", set1.union(set2))
# Set intersection
print("Intersection:", set1.intersection(set2))
# Set difference
print("Difference (set1 - set2):", set1.difference(set2))
# Set symmetric difference
print("Symmetric Difference:", set1.symmetric_difference(set2))
# Subset check
print("Is set1 subset of set2?:", set1.issubset(set2))
# Superset check
print("Is set1 superset of set2?:", set1.issuperset(set2))
# Disjoint check
print("Are set1 and set2 disjoint?:", set1.isdisjoint(set2))
# Copy a set
copy_set = set1.copy()
print("Copy of set1:", copy_set)