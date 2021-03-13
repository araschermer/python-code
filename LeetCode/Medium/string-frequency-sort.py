def frequency_sort(s: str) -> str:
    """
    a string, sort it in decreasing order based on the frequency of characters.
    :type s: str
    :rtype: str
    """
    result = ""
    string_dict = {str(char): 0 for char in s}
    for char in s:
        string_dict[char] += 1
    for char in range(len(string_dict)):
        if string_dict:
            max_key = max(string_dict, key = string_dict.get)
            for _ in range(string_dict[max_key]):
                result += max_key
            del string_dict[max_key]
    print(result)
    return result


# Example 1:
# Input: "tree" Output: "eert" Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'.
# Therefore "eetr" is also a valid answer.
frequency_sort("tree")
# Example 2:
# Input: "cccaaa" Output: "cccaaa"
# Explanation: Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
frequency_sort("cccaaa")
