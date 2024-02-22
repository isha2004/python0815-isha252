import math

# Get user input for N value and numbers
N = int(input("Enter N value: "))
if N < 2:
    print("Please enter at least two numbers.")
    exit()

numbers = []
for i in range(1, N+1):
    num = int(input(f"Number {i} = "))
    numbers.append(num)

# Calculate LCM and GCD without functions
lcm = numbers[0]
gcd = numbers[0]

for num in numbers[1:]:
    lcm = lcm * num // math.gcd(lcm, num)
    gcd = math.gcd(gcd, num)

# Output the results
print(f"LCM = {lcm}")
print(f"GCD = {gcd}")
