# Take input from the user
input_string = input("Enter a string: ")

# Remove vowels from the string
result_string = ''.join(char for char in input_string if char.lower() not in 'aeiou')

# Output the result
print(f"The string without vowels is: {result_string}")

