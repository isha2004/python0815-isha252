def permutations(lst):
    # If the list is empty, there are no permutations
    if not lst:
        return []

    # If there is only one element in lst, only one permutation is possible
    if len(lst) == 1:
        return [lst]

    result = []  # List to store permutations

    # Iterate over the elements of the list
    for i in range(len(lst)):
        m = lst[i]

        # Extract m from the list. rem_lst is the remaining list
        rem_lst = lst[:i] + lst[i+1:]

        # Generating all permutations where m is the first element
        for p in permutations(rem_lst):
            result.append([m] + p)

    return result

# Driver program to test above function
data = list(input("Enter a list of characters separated by spaces: "))
result_permutations = permutations(data)
for p in result_permutations:
    print(p)
