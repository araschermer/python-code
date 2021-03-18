def single_number( nums: [int]) -> int:
    """Given a non-empty array of integers nums, every element appears twice except for one. Find that single one. """
    # approach 01: runtime: o(n)
    # nums_dict hold the numbers  as keys and their frequency as value
    nums_dict = {num: 0 for num in nums}
    for num in nums:
        nums_dict[num] += 1
    # get the key that holds a value of 1 (single number/frequency of 1)
    single_num = [key for key, value in nums_dict.items() if value == 1]
    print(single_num[0])
    # return single_number[0]

    # Approach 02: runtime: o(n)
    # Runtime: 124 ms, faster than 94.64% of Python3 online submissions for Single Number.
    # Memory Usage: 16.5 MB, less than 86.39% of Python3 online submissions for Single Number.
    # since (n xor n)= 0  for any value of n
    # then, by XOR'ing all the values in num , only the single number remains
    single = 0
    for num in nums:
        single ^= num
    return single


# Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?
# Example 1: Input: nums = [2,2,1] Output: 1
assert single_number([2, 2, 1]), 1
# Example 2: Input: nums = [4,1,2,1,2] Output: 4
assert single_number([4, 1, 2, 1, 2]), 4
# Example 3: Input: nums = [1] Output: 1
assert single_number([1]), 1
