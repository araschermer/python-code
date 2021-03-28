def nextGreaterElement( nums1: [int], nums2: [int]) -> [int]:
    """Given two integer arrays nums1 and nums2 both of unique elements, where nums1 is a subset of nums2.
     return the number of the Next Greater Numbers: for a next greater number as a number in nums2
      that is greater in value than a number x of the exist in nums1
      If it does not exist, return -1 for this number."""
    result = []
    for number in nums1:
        index = nums2.index(number)
        next_greater = -1
        for num in nums2[index:]:
            if num > number:
                next_greater = num
                break
        result.append(next_greater)
    return result


if __name__ == "__main__":
    test_cases = [[[4, 1, 2], [1, 3, 4, 2]], [[2, 4], [1, 2, 3, 4]]]
# Example 1: Input: nums1 = [4,1,2], nums2 = [1,3,4,2] Output: [-1,3,-1]
# Explanation: For number 4 in the first array, you cannot find the next greater number for it in the second array,
# so output -1. For number 1 in the first array, the next greater number for it in the second array is 3.
# For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
#
# Example 2: Input: nums1 = [2,4], nums2 = [1,2,3,4] Output: [3,-1] Explanation: For number 2 in the first array,
# the next greater number for it in the second array is 3. For number 4 in the first array,
# there is no next greater number for it in the second array, so output -1.
    for test_case in test_cases:
        print(nextGreaterElement(test_case[0], test_case[1]))