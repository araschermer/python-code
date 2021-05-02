# Runtime: 220 ms, faster than 84.60% of Python3 online submissions for Count the Number of Consistent Strings.
# Memory Usage: 15.9 MB, less than 92.98% of Python3 online submissions for Count the Number of Consistent Strings.
# https://leetcode.com/submissions/detail/473423636/

def countConsistentStrings(allowed: str, words: [str]) -> int:
    """Given a string allowed consisting of distinct characters and an array of strings words.
     A string is consistent if all characters in the string appear in the string allowed.
     Return the number of consistent strings in the array words"""
    counter = 0
    for word in words:
        for char in word:
            valid = True
            if char not in allowed:
                print(char)
                valid = False
                break
        if valid:
            counter += 1
    print(counter)
    return counter


if __name__ == "__main__":
    # Example 1: # Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"], Output: 2
    # Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
    countConsistentStrings("ab",
                           ["ad", "bd", "aaab", "baa", "badab"])

    # Example 2: Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"], Output: 7
    # Explanation: All strings are consistent.
    countConsistentStrings("abc",
                           ["a", "b", "c", "ab", "ac", "bc", "abc"])

    # Example 3:  Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"], Output: 4
    # Explanation: Strings "cc", "acd", "ac", and "d" are consistent.
    countConsistentStrings("cad",
                           ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"])
