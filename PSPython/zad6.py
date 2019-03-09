
ROME_TABLE = [
    ("M", 1000), ("CM", 900), ("D", 500),
    ("CD", 400), ("C", 100),  ("XC", 90),
    ("L", 50),   ("XL", 40),  ("X", 10),
    ("IX", 9),   ("V", 5),    ("IV", 4),
    ("I", 1)
]


def integerToRome(base_ten):
    if base_ten > 3999:
        print("cannot transform")
        exit()
    elif base_ten < 0:
        print("cannot transform")
        exit()

    roman_numerals = []
    for numeral, value in ROME_TABLE:
        count = base_ten // value
        base_ten -= count * value
        roman_numerals.append(numeral * count)

    print(''.join(roman_numerals))
    return ''.join(roman_numerals)


if __name__ == '__main__':
    integerToRome(1234)

    


