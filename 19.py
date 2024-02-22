# Given binary numbers
binary_numbers = ['1101', '1011', '1001']

# Convert binary to decimal and find the maximum
max_decimal = max(int(binary, 2) for binary in binary_numbers)

# Convert the maximum decimal back to binary
max_binary = bin(max_decimal)[2:]

# Output the result
print(f"Given Numbers: {', '.join(binary_numbers)}")
print(f"Maximum Number: {max_binary}")
