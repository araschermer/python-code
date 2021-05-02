# https://leetcode.com/submissions/detail/466620736/
def merge(nums1, m, nums2, n):
    """
    Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array. The number of
    elements initialized in nums1 and nums2 are m and n respectively.
     You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """

    nums1[m:] = nums2
    nums1.sort()
    print(nums1)


merge([1, 2, 3, 0, 0, 0], m = 3, nums2 = [2, 5, 6], n = 3)
# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
merge(nums1 = [1], m = 1, nums2 = [], n = 0)
# Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
