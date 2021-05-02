from nose.tools import assert_equal


def two_sum(numbers: [int], target: int) -> [int]:
    """Given an array of integers numbers that is already sorted in ascending order,
    find two numbers such that they add up to a specific target number.
    Return the indices of the two numbers (1-indexed) as an integer array answer of size 2,
    where 1 <= answer[0] < answer[1] <= numbers.length. You may assume that each input would have exactly one solution
    and you may not use the same element twice."""
    for i in range(len(numbers) - 1):
        # if the array contains another number that  if adds to the element at index i equals target
        if (target - numbers[i]) in numbers:
            # get the index of that element
            # here the numbers array is sliced starting from the element after index i, just to disregard duplicates
            index = numbers[i + 1:].index(target - numbers[i])
            # return i+1 and the index the other element(in the original array numbers) +1
            # index+2+i : the index is from a subarray starting from index i+1, therefore i added i+1 to index+1
            return [i + 1, index + 2 + i]


if __name__ == '__main__':
    # Example 1:
    # Input: numbers = [2,7,11,15], target = 9
    # Output: [1,2]
    # Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
    assert_equal(two_sum([2, 7, 11, 15], 9), [1, 2])
    # Example 2:
    # Input: numbers = [2,3,4], target = 6
    # Output: [1,3]
    assert_equal(two_sum([2, 3, 4], 6), [1, 3])
    # Example 3:
    # Input: numbers = [-1,0], target = -1
    # Output: [1,2]
    assert_equal(two_sum([-1, 0], -1), [1, 2])

    assert_equal(two_sum([0, 0, 3, 4], 0), [1, 2])
    assert_equal(two_sum([5, 25, 75], 100), [2, 3])
