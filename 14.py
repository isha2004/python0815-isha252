# Given series
series = [1, 5, 11, 19]

# Find the missing numbers
missing_numbers = [series[i] + (i + 2) * 2 for i in range(len(series))]

# Output the result
print(f"The missing numbers in the series are: {missing_numbers}")
