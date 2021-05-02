def two_sum(nums, target):
    """Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add up to target
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # Check valid target:
    if type(target) is not int:
        raise TypeError('Target is not an integer!')
    # check the type of the nums elements :
    for index, num in enumerate(nums):
        if type(num) is not int:
            raise TypeError(f"{num} Invalid number type in the input array")
        # check non-repetitiveness in the array
        if num in nums and nums.index(num) != index:
            raise ValueError("Array contains repetitive numbers")

    # coping the array's content in an external  array to keep the indices intact in the original nums array
    sorted_nums = nums[:]
    # sorting the elements of the array
    sorted_nums.sort()
    first_pointer = 0
    last_pointer = -1
    result = []
    for _ in range(len(sorted_nums)):
        first_number = sorted_nums[first_pointer]
        second_number = sorted_nums[last_pointer]
        if (first_number + second_number) > target:
            last_pointer -= 1
        if (first_number + second_number) < target:
            first_pointer += 1
        if (first_number + second_number) == target and first_number != second_number:
            result = [index for index in range(len(nums)) if
                      nums[index] == sorted_nums[first_pointer] or nums[index] == sorted_nums[last_pointer]]
            break
    return result


if __name__ == '__main__':
    print(two_sum([2, 7, 11, 15], 9))
    print(two_sum([3, 2, 4], 6))
    print(two_sum([3, 3], 6))

    # Example 1:
    # Input: nums = [2,7,11,15], target = 9
    # Output: [0,1]
    # Output: Because nums[0] + nums[1] == 9, we return [0, 1].

    # Example 2:
    # Input: nums = [3,2,4], target = 6
    # Output: [1,2]

    # Example 3:
    # Input: nums = [3,3], target = 6
    # Output: [0,1]
