from nose.tools import assert_equal


def three_sum_closest(nums: [int], target: int) -> int:
    """Given an array nums of n integers and an integer target, find three integers in nums such that the sum is
    closest to target. Return the sum of the three integers. You may assume that each input would have exactly one
    solution. """
    if len(nums) < 3:
        return -1
    # get the sum of the first two elements of the array and the last element
    closest_sum = nums[0] + nums[1] + nums[-1]
    #  sort the array to have the biggest number on the left and the smallest number on the right
    nums.sort()
    # iterate through the array
    for i in range(0, len(nums) - 2):
        # left pointer: to the right of the current position
        left = i + 1
        # right pointer: the starting with the biggest number in the array
        right = len(nums) - 1
        # if there are more elements left between the pointers
        while left < right:
            # if  current sum equals target, return closest sum
            if closest_sum == target:
                return closest_sum
            # sum elements at indices i, left, and right
            temp = nums[i] + nums[left] + nums[right]
            # if the previous sum is bigger than target: move right pointer to the left by one position
            if temp > target:
                right -= 1
            else:
                # else: meaning the current sum is smallest than target: move left pointer to the right by one position
                left += 1
            # if the current sum is  closer to target than the closest sum: then closest sum=current sum
            if abs(target - temp) < abs(target - closest_sum):
                closest_sum = temp
    return closest_sum


if __name__ == '__main__':
    assert_equal(three_sum_closest([1, 1, 1, 0], -100), 2)
    assert_equal(three_sum_closest([-1, 2, 1, -4], -3), -3)
    assert_equal(three_sum_closest([0, 2, 1, -3], 1), 0)
    assert_equal(three_sum_closest([1, 2, -100, 10, -100], 0), 13)
    assert_equal(three_sum_closest([1, 2, -100, 10, -100], -50), -88)
    assert_equal(three_sum_closest([1, 2, -100, 10, -100], -150), -190)
    assert_equal(three_sum_closest([1, 1, -1, -1, 3], 3), 3)
