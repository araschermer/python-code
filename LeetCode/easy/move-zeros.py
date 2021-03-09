def move_zeroes(nums):
    """Given an array nums, write a function to move all 0's to the end of it
     while maintaining the relative order of the non-zero elements.
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    # approach 01
    zero_counter = 0
    while 0 in nums:
        nums.remove(0)
        zero_counter += 1
    while zero_counter > 0:
        nums.append(0)
        zero_counter -= 1
    print(nums)

    # approach 02: faster than approach 01
    zero_tracker = 0
    for index, num in enumerate(nums):
        if num != 0 and zero_tracker != index:
            nums[zero_tracker], nums[index] = nums[index], nums[zero_tracker]
            zero_tracker += 1
        elif num != 0:
            zero_tracker += 1
    print(nums)


if __name__ == '__main__':
    move_zeroes([0, 2, 0, 2, 0, 8, 0, 4, 9])
    move_zeroes([0, 4, 9])
    move_zeroes([9, 0])
    move_zeroes([0, 1, 0, 3, 12])
