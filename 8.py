# Get user input for a word
word = input("Enter the word: ")

# Arrange letters in reverse alphabetical order
sorted_word = ''.join(sorted(word, reverse=True))

# Output the result
print(f"Original Word: {word}")
print(f"Alphabetical Order (Reverse): {sorted_word}")
