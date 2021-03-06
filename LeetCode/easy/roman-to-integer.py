def roman_to_int(s):
    """ Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
            roman_integer_value = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII,
    which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
    Roman numerals are usually written largest to smallest from left to right.
    However, the numeral for four is not IIII. Instead, the number four is written as IV.
    Because the one is before the five we subtract it making four. The same principle applies to the number nine,
    which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.
    Given a roman numeral, convert it to an integer
    :type s: str
    :rtype: int
    """
    integer_value = 0
    for index, char in enumerate(s):
        if char == "I":
            integer_value += 1
        elif char == "V":
            integer_value += 5
        elif char == "X":
            integer_value += 10
        elif char == "L":
            integer_value += 50
        elif char == "C":
            integer_value += 100
        elif char == "D":
            integer_value += 500
        elif char == "M":
            integer_value += 1000
        if index >= 1 and (s[index - 1] == "I" and char in ["X", "V"]):  # not out of bound check,
            # and check if previous character is not I and the current current character is neither "X" nor "V",
            # if so, decrement integer_value by 2. example : "IX" is 9, here we calculated "I"+"X"=11
            # after decrementing the integer_value it becomes 9 again
            integer_value -= 2
        if index >= 1 and (s[index - 1] == "X" and char in ["L", "C"]):
            integer_value -= 20
        if index >= 1 and (s[index - 1] == "C" and char in ["M", "D"]):
            integer_value -= 200
    print(integer_value)
    return integer_value


if __name__ == '__main__':
    # Example 1:
    # Input: s = "III"
    # Output: 3
    roman_to_int("III")
    # Example 2:
    # Input: s = "IV"
    # Output: 4
    roman_to_int("IV")

    # Example 3:
    # Input: s = "IX"
    # Output: 9
    roman_to_int("IX")

    # Example 4:
    # Input: s = "LVIII"
    # Output: 58
    # Explanation: L = 50, V= 5, III = 3.
    roman_to_int("LVIII")

    # Example 5:
    # Input: s = "MCMXCIV"
    # Output: 1994
    # Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
    roman_to_int("MCMXCIV")
