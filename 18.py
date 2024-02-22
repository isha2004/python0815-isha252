# Take input from the user
number = int(input("Enter a number: "))

# Check if the input number is prime
if number < 2:
    result = False
else:
    is_prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    result = is_prime

# Output the result
print(f"Input number: {number}")
print(f"Output: {result}")
