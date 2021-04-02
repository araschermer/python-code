from nose.tools import assert_equal


def three_sum(nums: [int]) -> [[int]]:
    """Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k,
     and j != k, and nums[i] + nums[j] + nums[k] == 0.
     Notice that the solution set must not contain duplicate triplets."""
    if len(nums) <= 2:
        return []
    nums.sort()
    result = []
    for i in range(len(nums)):
        left = i
        middle = left + 1
        right = len(nums) - 1
        while left < right and middle < right:
            first = nums[left]
            second = nums[middle]
            third = nums[right]
            if first + second + third > 0:
                right -= 1
                continue
            elif first + second + third == 0:
                if [first, second, third] not in result:
                    result.append([first, second, third])
            middle += 1
    return result


if __name__ == "__main__":
    # Example 1:
    # Input: nums = [-1,0,1,2,-1,-4]
    # Output: [[-1,-1,2],[-1,0,1]]
    assert_equal(three_sum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])

    # Example 2:
    # Input: nums = []
    # Output: []
    assert_equal(three_sum([]), [])
    # Example 3
    # Input: nums = [0]
    # Output: []
    assert_equal(three_sum([0]), [])

    assert_equal(three_sum([0, 0, 0, 0]), [[0, 0, 0]])
    assert_equal(three_sum([0, 0, 0]), [[0, 0, 0]])
    assert_equal(three_sum([-2, 0, 1, 1, 2]), [[-2, 0, 2], [-2, 1, 1]])
