# Memory Usage: 13.2 MB, less than 99.39% of Python online submissions for Remove Element.
# https://leetcode.com/submissions/detail/465653328/
def remove_element(nums, val):
    """
    Given an array nums and a value val, remove all instances of that value in-place and return the new length.
    Do not allocate extra space for another array, you must do this by modifying
    the input array in-place with O(1) extra memory. The order of elements can be changed.
    It doesn't matter what you leave beyond the new length.
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    while val in nums:
        nums.remove(val)
    return len(nums)


if __name__ == '__main__':
    assert (remove_element([1, 2, 3, 4, 5, 3, 5, 7, 6], 5) == 7)
    assert (remove_element([3, 2, 2, 3], 3) == 2)
    assert (remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5)
