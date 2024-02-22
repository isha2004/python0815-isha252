 #Get user input for statement
statement = input("Enter a statement: ")

# Initialize the vowel count to 0
vowel_count = 0;

 #Iterate over each character in the statement
for char in statement:
    # Check the character is a vowel
    if char.lower() in "aeiou":
        # Increment the vowel count
        vowel_count += 1

# Output the result
print(f"Number of vowels = {vowel_count}")