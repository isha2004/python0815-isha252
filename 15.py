# Input string
a = "This is a cat"

# Extract the first letter of each word and join them
output = '.'.join(word[0].upper() for word in a.split())

# Output the result
print(f"Input: {a}")
print(f"Output: {output}")
