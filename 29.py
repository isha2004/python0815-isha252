class PowerCalculator:
    def pow(self, x, n):
        # Base case: x^0 is always 1
        if n == 0:
            return 1

        # For negative exponents, calculate reciprocal and negate the exponent
        if n < 0:
            x = 1 / x
            n = -n

        result = 1
        while n > 0:
            # If n is odd, multiply result by x
            if n % 2 == 1:
                result *= x

            # Update x to x^2 and halve n
            x *= x
            n //= 2

        return result