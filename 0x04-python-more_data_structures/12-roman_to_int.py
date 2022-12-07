#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    rom = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    no = 0
    for i in range(0, len(roman_string)):
        k = roman_string[i]
        if k in rom:
            if i < len(roman_string) - 1 and rom[k] < rom[roman_string[i + 1]]:
                no -= rom[k]
            else:
                no += rom[k]
    return no
