def running_sum(nums):
    """Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
    Return the running sum of nums.
    Example 1: Input: nums = [1,2,3,4] Output: [1,3,6,10]
    Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
    Example 2: Input: nums = [1,1,1,1,1] Output: [1,2,3,4,5] Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
    Example 3: Input: nums = [3,1,2,10,1] Output: [3,4,6,16,17]
    :type nums: List[int]
    :rtype: List[int]

    """
    # https://leetcode.com/submissions/detail/466562475/
    # runtime beats 80.92 % of python submissions.
    # memory usage beats 98.99 % of python submissions.

    r_sum = nums[0]
    for index in range(1, len(nums)):
        r_sum += nums[index]
        nums[index] = r_sum
    return nums


print(running_sum([1, 2, 3, 4]))
print(running_sum([1, 1, 1, 1, 1]))
print(running_sum([3, 1, 2, 10, 1]))
