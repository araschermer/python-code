from numpy.testing import assert_equal


def four_number_sum(nums: [int], target) -> [[int]]:
    """Returns all possible combinations (without duplicates) of all elements in nums that sum up to target.
    """
    nums.sort()
    result = []
    two_sum_table = {}
    for index1 in range(1, len(nums) - 1):
        for index2 in range(index1 + 1, len(nums)):
            current_two_sum = nums[index1] + nums[index2]
            difference = target - current_two_sum
            if difference in two_sum_table:
                for pair in two_sum_table[difference]:
                    result.append(pair + [nums[index1], nums[index2]])
        for index2 in range(0, index1):
            current_two_sum = nums[index1] + nums[index2]
            if current_two_sum not in two_sum_table:
                two_sum_table[current_two_sum] = [[nums[index1], nums[index2]]]
            else:
                two_sum_table[current_two_sum].append([nums[index1], nums[index2]])
    # remove duplicates
    results = []
    for quadruplet in result:
        if quadruplet not in results:
            results.append(quadruplet)
    # sort the elements of each quadruplet in the results
    for index in range(len(results)):
        results[index] = sorted(results[index])
    return results


assert_equal(four_number_sum([-1, -5, -5, -3, 2, 5, 0, 4], -7), [[-5, -3, -1, 2], [-5, -5, -1, 4]])
assert_equal(four_number_sum([-3, -2, -1, 0, 0, 1, 2, 3], 0), [[-2, -1, 0, 3], [-1, 0, 0, 1], [-2, 0, 0, 2],
                                                               [-3, 0, 0, 3], [-2, -1, 1, 2], [-3, 0, 1, 2],
                                                               [-3, -1, 1, 3], [-3, -2, 2, 3]])
assert_equal(four_number_sum([7, 6, 4, -1, 1, 2], 16), [[1, 2, 6, 7], [-1, 4, 6, 7]])
assert_equal(four_number_sum([-1, 1, 1, -2, 0, 7, 6, 4, -1, 1, 2], 0), [[-2, -1, -1, 4], [-1, -1, 0, 2], [-1, -1, 1, 1],
                                                                        [-2, 0, 1, 1], [-2, -1, 1, 2]])
assert_equal(four_number_sum([1, 0, -1, 0, -2, 2], 0), [[-1, 0, 0, 1], [-2, 0, 0, 2], [-2, -1, 1, 2]])
assert_equal(four_number_sum([2, 2, 2, 2, 2], 8), [[2, 2, 2, 2]])
assert_equal(four_number_sum([-3, -1, 0, 2, 4, 5], 0), [[-3, -1, 0, 4]])
assert_equal(four_number_sum([-2, -1, -1, 1, 1, 2, 2], 0), [[-1, -1, 1, 1], [-2, -1, 1, 2]])
