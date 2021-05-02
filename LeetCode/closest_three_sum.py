from nose.tools import assert_equal


def closest_three_sum(nums: [int], target: int) -> int:
    """Given an array nums of n integers and an integer target,
     find three nearby integers in nums such that the sum is closest to target. Return the sum of the three integers.
      You may assume that each input would have exactly one solution."""
    if len(nums) < 3:
        return -1
    closest = nums[0] + nums[1] + nums[2]
    for i in range(1, len(nums) - 2):
        temp = nums[i] + nums[i + 1] + nums[i + 2]
        print(f"temp = {temp}")
        print(f"closest={closest}")
        if abs(target - temp) < abs(target - closest):
            closest = temp
    return closest


if __name__ == '__main__':
    assert_equal(closest_three_sum([1, 1, 1, 0], -100), 2)
    # # three_sum_closest([1, 1, 1, 0], -100)
    assert_equal(closest_three_sum([-1, 2, 1, -4], -3), -1)
    assert_equal(closest_three_sum([0, 2, 1, -3], 1), 0)
    assert_equal(closest_three_sum([1, 2, -100, 10, -100], 0), -88)
    assert_equal(closest_three_sum([1, 2, -100, 10, -100], -50), -88)
    assert_equal(closest_three_sum([1, 2, -100, 10, -100], -150), -190)
    assert_equal(closest_three_sum([1, 1, -1, -1, 3], 3), 1)
