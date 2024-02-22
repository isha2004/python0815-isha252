def reverse_word(word):
    reversed_word = ''
    for i in range(len(word) - 1, -1, -1):
        reversed_word += word[i]
    return reversed_word

# Get user input for a word
user_input = input("Enter a word: ")
reversed_output = reverse_word(user_input)

# Output the result
print(f"Original Word: {user_input}")
print(f"Reversed Word: {reversed_output}")