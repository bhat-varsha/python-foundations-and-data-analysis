# Get input names from user
name1 = input("Enter the first name: ").lower()
name2 = input("Enter the second name: ").lower()

# Combine names
combined_names = name1 + name2

# Count letters in "TRUE"
true_count = 0
for letter in "true":
    true_count += combined_names.count(letter)

# Count letters in "LOVE"
love_count = 0
for letter in "love":
    love_count += combined_names.count(letter)

# Combine counts into a 2-digit number
love_score = int(str(true_count) + str(love_count))

# Print result
print(f"Your love score is: {love_score}")