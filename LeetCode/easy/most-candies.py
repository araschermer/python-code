def kids_with_candies(candies: [int], extra_candies: int) -> [bool]:
    """Given the array candies and the integer extraCandies,
     where candies[i] represents the number of candies that the ith kid has.
      For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have
       the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies."""

    # Approach 01:
    # Runtime: 40 ms, faster than 57.65% of Python3 online submissions for Kids With the Greatest Number of Candies.

    # result = []
    # most_candy = max(candies)
    # for candy in candies:
    #     if candy + extra_candies >= most_candy:
    #         result.append(True)
    #     else:
    #         result.append(False)
    # return result

    # Approach 02 : Runtime: 40 ms, faster than 57.65% of Python3 online submissions for Kids With the Greatest
    # Number of Candies. Memory Usage: 14.1 MB, less than 82.37% of Python3 online submissions for Kids With the
    # Greatest Number of Candies.
    # return [True if candy + extra_candies >= max(candies) else False for candy in candies]

    # Approach 03:
    # Runtime: 28 ms, faster than 98.80% of Python3 online submissions for Kids With the Greatest Number of Candies.
    # https://leetcode.com/submissions/detail/467633670/
    max_candies = max(candies)
    return [candy + extra_candies >= max_candies for candy in candies]


# Example 1:
# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true]
# Explanation: Kid 1 has 2 candies and if he or she receives all extra candies (3) will have 5 candies ---
# the greatest number of candies among the kids.
# Kid 2 has 3 candies and if he or she receives at least 2 extra candies
# will have the greatest number of candies among the kids.
# Kid 3 has 5 candies and this is already the greatest number  of candies among the kids.
# Kid 4 has 1 candy and even if he or she receives all extra candies will only have 4 candies.
# Kid 5 has 3 candies and if he or she receives at least 2 extra candies will have
# the greatest number of candies among the kids.
print(kids_with_candies([2, 3, 5, 1, 3], 3))

# Example 2: Input: candies = [4,2,1,1,2], extraCandies = 1 Output: [true,false,false,false,false]
# Explanation: There is only 1 extra candy, therefore only kid 1 will have the greatest number of candies
# among the kids regardless of who takes the extra candy.
# Example 3: Input: candies = [12,1,12], extraCandies = 10 Output: [true,false,true]
print(kids_with_candies([4, 2, 1, 1, 2], 1))
