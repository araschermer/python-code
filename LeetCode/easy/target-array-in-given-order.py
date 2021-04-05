from nose.tools import assert_equal


def create_target_array(nums: [int], index: [int]) -> [int]:
    """Given two arrays of integers nums and index. Your task is to create target array under the following rules:
    Initially target array is empty.From left to right read nums[i] and index[i],
    insert at index index[i] the value nums[i] in target array.
    Repeat the previous step until there are no elements to read in nums and index.Return the target array.
    It is guaranteed that the insertion operations will be valid."""
    result = []
    for index_, num in zip(index, nums):
        result.insert(index_, num)
    # Alternative:
    # for i, index_ in enumerate(index):
    #     result.insert(index_, nums[i])

    return result


if __name__ == "__main__":
    # Example 1:
    # Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
    # Output: [0,4,1,3,2]
    # Explanation:
    # nums       index     target
    # 0            0        [0]
    # 1            1        [0,1]
    # 2            2        [0,1,2]
    # 3            2        [0,1,3,2]
    # 4            1        [0,4,1,3,2]
    assert_equal(create_target_array([0, 1, 2, 3, 4], [0, 1, 2, 2, 1]), [0, 4, 1, 3, 2])
    # Example 2:
    # Input: nums = [1,2,3,4,0], index = [0,1,2,3,0]
    # Output: [0,1,2,3,4]
    # Explanation:
    # nums       index     target
    # 1            0        [1]
    # 2            1        [1,2]
    # 3            2        [1,2,3]
    # 4            3        [1,2,3,4]
    # 0            0        [0,1,2,3,4]
    assert_equal(create_target_array(nums=[1, 2, 3, 4, 0], index=[0, 1, 2, 3, 0]), [0, 1, 2, 3, 4])
    # Example 3:
    #
    # Input: nums = [1], index = [0]
    # Output: [1]
    assert_equal(create_target_array([1], [0]), [1])
