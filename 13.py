# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Compare the numbers to find the largest
if num1 >= num2 and num1 >= num3:
    max_value = num1
elif num2 >= num1 and num2 >= num3:
    max_value = num2
else:
    max_value = num3

# Output the result
print(f"The largest value among {num1}, {num2}, and {num3} is: {max_value}")
