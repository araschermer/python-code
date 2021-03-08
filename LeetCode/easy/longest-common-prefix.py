def longest_common_prefix(strs):
    """Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string
    https://leetcode.com/submissions/detail/465245104/
    #Runtime: 16 ms, faster than 94.96% of Python online submissions for Longest Common Prefix.
    #Memory Usage: 13.6 MB, less than 91.37% of Python online submissions for Longest Common Prefix.
    :type strs: List[str]
    :rtype: str
    """

    if len(strs) == 0:
        return ""
    prefix = strs[0]
    for string in strs:
        while prefix not in string[0:len(prefix)] and prefix != "":
            prefix = prefix[:-1]
    print(prefix)
    return prefix


if __name__ == "__main__":
    longest_common_prefix(["flower", "flow", "flight"])
    longest_common_prefix(["dog", "racecar", "car"])
    longest_common_prefix(["c", "acc", "ccc"])
    longest_common_prefix(["aaa","aa","aaa"])
    longest_common_prefix(["abab","aba","abc"])

