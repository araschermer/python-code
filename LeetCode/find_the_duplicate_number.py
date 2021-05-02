# Runtime: 64 ms, faster than 76.99% of Python3 online submissions for Find the Duplicate Number.
def find_duplicate(nums: [int]) -> int:
    """Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
    There is only one repeated number in nums, return this repeated number. """
    nums_dict = {num: 0 for num in nums}
    for num in nums:
        nums_dict[num] += 1  # increace frequency of each key(nums element) in the nums_dict
        if nums_dict[num] == 2:  # if frequency =2-> num is duplicated
            return num


# Example 1: Input: nums = [1,3,4,2,2] Output: 2
assert find_duplicate([1, 3, 4, 2, 2]), 2
# Example 2: Input: nums = [3,1,3,4,2] Output: 3
assert find_duplicate([3, 1, 3, 4, 2]), 3
# Example 3: Input: nums = [1,1] Output: 1
assert find_duplicate([1, 1]), 1
# Example 4: Input: nums = [1,1,2] Output: 1
assert find_duplicate([1, 1, 2]), 1
