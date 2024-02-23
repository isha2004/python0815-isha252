class IntegerToRoman:
    def __init__(self):
        self.integer_to_roman_mapping = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]

    def convert(self, num):
        if not isinstance(num, int) or not 0 < num < 4000:
            raise ValueError("Input must be an integer between 1 and 3999")

        result = ""
        for value, roman in self.integer_to_roman_mapping:
            while num >= value:
                result += roman
                num -= value

        return result