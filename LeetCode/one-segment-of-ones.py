import re


# mu submission: https://leetcode.com/submissions/detail/465216555/
# Runtime: 16 ms, faster than 100.00% of Python
# online submissions for Check if Binary String Has at Most One Segment of Ones. Memory Usage: 13.5 MB,
# less than 100.00% of Python online submissions for Check if Binary String Has at Most One Segment of Ones.

def check_ones_segment(s):
    """
        Given a binary string s without leading zeros, return true,
         if s contains at most one contiguous segment of ones.
          Otherwise, return false.
    """
    strings = ["11", "111"]
    result = False
    if re.search("10+1", s):  # if the string contains any form two ones split by 0, then return false
        return False
    for index, value in enumerate(s):
        # to catch the cases of the repetitive ones
        if index < (len(s) - 2) and value + s[index + 1] + s[index + 2] in strings:
            result = not result
        if index < (len(s) - 1) and value + s[index + 1] in strings:
            result = not result
    if not result:
        list_s = [int(i) for i in s]
        if sum(list_s) == 1:
            return True
    return result


if __name__ == "__main__":
    print(check_ones_segment("1110001001"))
    print(check_ones_segment("1101"))
    print(check_ones_segment("110110"))
    print(check_ones_segment("110"))
    print(check_ones_segment("10"))
    print(check_ones_segment("1"))
