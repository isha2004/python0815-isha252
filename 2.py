# Get user input for a sorted array
user_input = input("Enter a sorted array of numbers separated by spaces: ")
user_array = list(map(int, user_input.split()))

# Remove duplicates in-place
unique_array = [user_array[0]]

for i in range(1, len(user_array)):
    if user_array[i] not in unique_array:
        unique_array.append(user_array[i])

# Output the result
print(f"Sorted Array with Duplicates Removed: {unique_array}")