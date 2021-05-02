# Runtime: 120 ms, faster than 96.69% of Python3 online submissions for Missing Number.
# Memory Usage: 15.3 MB, less than 82.71% of Python3 online submissions for Missing Number.
def missing_number(nums: [int]) -> int:
    """Given an array nums containing n distinct numbers in the range [0, n], return the only number
    in the range that is missing from the array."""
    # since all the numbers in nums are distinct and  the missing number is  in range 0,n
    # then summing over the range 0,n would give us the  sum of nums+ the missing number
    range_nums_sum = [i for i in range(len(nums) + 1)]
    range_nums_sum = sum(range_nums_sum)
    # subtracting sum(nums) form sum of the range value would give us the missing number
    return range_nums_sum - sum(nums)


# Example 1: Input: nums = [3,0,1] Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
# 2 is the missing number in the range since it does not appear in nums.
assert missing_number([3, 0, 1]), 2
# Example 2: Input: nums = [0,1] Output: 2 Explanation: n = 2 since there are 2 numbers,
# so all numbers are in the range [0,2].
# 2 is the missing number in the range since it does not appear in nums.
assert missing_number([0, 1]), 2
# Example 3: Input: nums = [9,6,4,2,3,5,7,0,1] Output: 8 Explanation: n = 9 since there are 9 numbers,
# so all numbers are in the range [0,9].
# 8 is the missing number in the range since it does not appear in nums.
assert missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8
# Example 4: Input: nums = [0] Output: 1 Explanation: n = 1 since there is 1 number,
# so all numbers are in the range [0,1].
# 1 is the missing number in the range since it does not appear in nums.
