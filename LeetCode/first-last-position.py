# Runtime: 80 ms, faster than 90.25% of Python3 online submissions for Find First and Last Position of Element in
# Sorted Array.
# Memory Usage: 15.3 MB, less than 82.68% of Python3 online submissions for Find First and Last
# Position of Element in Sorted Array.
def search_range(nums, target):
    """Given an array of integers nums sorted in ascending order, find the starting and ending position of a given
    target value. If target is not found in the array, return [-1, -1].
    :type nums: List[int]
    :type target: int
    :rtype: List[int]"""
    if target not in nums or not nums:
        return [-1, -1]
    pos = -1
    starting_pos = 0
    ending_pos = 0
    for index, num in enumerate(nums):
        if num != target and ending_pos == 0:
            pos = index
        elif target == num:
            starting_pos = pos + 1
            ending_pos = index
    return [starting_pos, ending_pos]


print(search_range([0, 1, 1, 1], 1)) # [1,3]
print(search_range([5, 7, 7, 8, 8, 10], 8)) # [3,4]
print(search_range([5, 7, 7, 8, 8, 10], 6)) # [-1,-1]
print(search_range([], 0)) # [-1,-1]
print(search_range([1], 1)) # [0,0]
