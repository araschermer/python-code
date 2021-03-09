def remove_duplicates(nums):
    """Remove duplicated from a sorted array.
    Given a sorted array nums, remove the duplicates in-place such that each element appears only once
    and returns the new length.
    Do not allocate extra space for another array,
    you must do this by modifying the input array in-place with O(1) extra memory.
    Clarification:Confused why the returned value is an integer but your answer is an array?
    Note that the input array is passed in by reference,
     which means a modification to the input array will be known to the caller as well."""
    if len(nums) in [0, 1]:  # if a sorted array has 1 or two elements, then no duplicates exist in this array
        return len(nums)
    start_index = 1
    while start_index < len(nums):
        if nums[-start_index] == nums[-start_index - 1]:  # start from the end
            # if the last element and the previous to the last are equal
            nums.remove(nums[-start_index])  # remove the last element
        else:
            start_index += 1  # move to the previous element
    print(len(nums))
    return len(nums)


if __name__ == "__main__":
    assert(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5)
    assert(remove_duplicates([1, 1, 2]) == 2)
