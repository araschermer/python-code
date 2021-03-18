# Runtime: 176 ms, faster than 97.52% of Python3 online submissions for Set Mismatch.
# Memory Usage: 15.9 MB, less than 42.22% of Python3 online submissions for Set Mismatch.
def find_error_nums(nums: [int]) -> [int]:
    """You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately,
    due to some error, one of the numbers in s got duplicated to another number in the set, which results in
    repetition of one number and loss of another number. You are given an integer array nums representing the data
    status of this set after the error. Find the number that occurs twice and the number that is missing and return
    them in the form of an array. """
    # since we  that  all the number are between 1 and n, one number is missing and another is repeated twice
    # then the sum of the set(nums) would give us the sum of all nums in nums - the repeated number
    # ( since a set does not store repeated numbers) -> from that we get the repeated number
    nums_set_sum = sum(set(nums))
    repeated_num = sum(nums) - nums_set_sum
    # if we subtract the sum  of the set of the given numbers from the sum of all numbers in range 0,n
    # we obtain the missing number
    missing_num = sum(i for i in range(len(nums) + 1)) - nums_set_sum
    # return  repeated_num and missing_num
    return [repeated_num, missing_num]


# Example 1:
# Input: nums = [1,2,2,4]
# Output: [2,3]
assert find_error_nums([1, 2, 2, 4]), [2, 3]
# Example 2:
# Input: nums = [1,1]
# Output: [1,2]
assert find_error_nums([1, 1]), [1, 2]
