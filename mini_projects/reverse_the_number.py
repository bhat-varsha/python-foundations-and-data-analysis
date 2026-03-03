# Take input from user and convert it to integer
num = int(input("Enter a number: "))

# Initialize variable to store the reversed number
rev = 0

# Use a temporary variable so the original number is not lost
temp = num

# Loop until all digits of temp are processed
while temp > 0:
    # Get the last digit of temp
    digit = temp % 10

    # Append the last digit to rev (shift previous digits left)
    rev = rev * 10 + digit

    # Remove the last digit from temp
    temp = temp // 10

# Print the reversed number
print("Reversed number:", rev)
