# Runtime: 176 ms, faster than 96.05% of Python online submissions for Squares of a Sorted Array.
# Memory Usage: 15.2 MB, less than 98.60% of Python online submissions for Squares of a Sorted Array.
# https://leetcode.com/submissions/detail/466622131/

def sorted_squares(nums):
    """Given an integer array nums sorted in non-decreasing order,
     return an array of the squares of each number sorted in non-decreasing order.
    :type nums: List[int]
    :rtype: List[int]
    """
    for i in range(len(nums)):
        nums[i] *= nums[i]
    return sorted(nums)


print(sorted_squares([-4, -1, 0, 3, 10]))
# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
print(sorted_squares([-7, -3, 2, 3, 11]))
# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
