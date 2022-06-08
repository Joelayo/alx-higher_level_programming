#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or len(roman_string) is 0:
        return 0
    letters = roman_string
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    elem = 0
    convention = 0
    while elem < len(letters):
        if elem < len(letters) - 1 and dic[letters[elem]] < dic[letters[elem+1]]:
            convention -= dic[letters[elem]]
        else:
            convention += dic[letters[elem]]
        elem += 1
    return convention
