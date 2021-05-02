from LeetCode.util import check_validity


def two_sum(nums, target):
    """Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add up to target
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # Time complexity is o(n log n) because of the array sorting, space complexity: o(n): for using the sorted array
    check_validity(nums, target)

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


def two_sums(nums, target):
    """Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add up to target
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # time complexity is o(n^2), space complexity is o(1)
    check_validity(nums, target)
    result = []
    for index1, num1 in enumerate(nums):
        for index2, num2 in enumerate(nums):
            if num1 != num2 and num1 + num2 == target:
                result = [index1, index2]
    return result


def two_sums_(nums, target):
    """Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add up to target
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # time complexity is o(n), space complexity is O(n)
    check_validity(nums, target)
    nums_table = {}
    for index, num in enumerate(nums):
        if target - num in nums_table:
            return [nums_table[target - num], index]
        else:
            nums_table[num] = index
    return []


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
