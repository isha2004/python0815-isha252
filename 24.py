fib_series = [0, 1]
n = int(input("Enter the number of Fibonacci numbers to generate: "))

while len(fib_series) < n:
    fib_series.append(fib_series[-1] + fib_series[-2])

print(f"Fibonacci numbers up to {n} terms: {fib_series}")
