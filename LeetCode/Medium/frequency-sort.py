def frequency_sort(nums: [int]) -> [int]:
    """Given an array of integers nums, sort the array in increasing order based on the frequency of the values.
     If multiple values have the same frequency, sort them in decreasing order. Return the sorted array.
    """
    nums.sort(reverse = True)
    nums_dict = {number: 0 for number in nums}
    for num in nums:
        nums_dict[num] += 1
    result = []
    for num in range(len(nums_dict)):
        if nums_dict:
            min_key = min(nums_dict, key = nums_dict.get)
            for _ in range(nums_dict[min_key]):
                result.append(min_key)
            del nums_dict[min_key]
    print(result)
    return result


# Example 1:
# Input: nums = [1,1,2,2,2,3]
# Output: [3,1,1,2,2,2]
# Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
frequency_sort([1, 1, 2, 2, 2, 3])
# Example 2:
# Input: nums = [2,3,1,3,2]
# Output: [1,3,3,2,2] Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.
# Example 3: Input: nums = [-1,1,-6,4,5,-6,1,4,1] Output: [5,-1,4,4,-6,-6,1,1,1]
frequency_sort([2,3,1,3,2] )