class RomanConverter:
    def int_to_roman(self, number):
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman_num = ''
        i = 0
        while number > 0:
            for _ in range(number // val[i]):
                roman_num += syms[i]
                number -= val[i]
            i += 1
        return roman_num

converter = RomanConverter()
num = int(input("Enter an integer: "))
print("Roman numeral:", converter.int_to_roman(num))
