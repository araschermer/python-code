# Runtime: 48 ms, faster than 99.95% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 15.2 MB, less than 15.44% of Python3 online submissions for Maximum Subarray.

def max_sub_array(nums):
    """Given an integer array nums, find the contiguous subarray (containing at least one number)
    which has the largest sum and return its sum."""
    max_sum = float("-inf")# unbounded lower value
    # https://stackoverflow.com/questions/34264710/what-is-the-point-of-floatinf-in-python
    # max_sum = sum(nums)
    # max_sum=nums[0]
    running_sum = 0
    for num in nums:
        if num + running_sum > num:  # accumulating the maximum value possible of the running sum
            running_sum = num + running_sum
        else:
            running_sum = num  # resets the running sum to num>running_sum, i.e. if num>= running_sum+num
        if running_sum > max_sum:  # a running sum can only replace the max_sum, if it is clearly greater than its value
            max_sum = running_sum
    return max_sum


# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
assert max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6

# Example 2:
# Input: nums = [1]
# Output: 1
assert max_sub_array([1]), 1

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23
assert max_sub_array([5, 4, -1, 7, 8]), 23
