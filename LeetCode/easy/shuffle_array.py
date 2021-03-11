def shuffle(nums, n):
    """
    Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
     Return the array in the form [x1,y1,x2,y2,...,xn,yn].
    :type nums: List[int]
    :type n: int
    :rtype: List[int]
    """
    # Runtime: 44 ms, faster than 74.03% of Python online submissions for Shuffle the Array.
    # Memory Usage: 13.4 MB, less than 99.37% of Python online submissions for Shuffle the Array.
    # https://leetcode.com/submissions/detail/466615090/
    num = []
    for i in range(n):
        num.append(nums[i])
        num.append(nums[n + i])
    print(num)
    return num


shuffle([2, 5, 1, 3, 4, 7], 3)
# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7]
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4)
# Example 2:
# Input: nums = [1,2,3,4,4,3,2,1], n = 4
# Output: [1,4,2,3,3,2,4,1]
shuffle([1, 1, 2, 2], 2)
# Example 3:
# Input: nums = [1,1,2,2], n = 2
# Output: [1,2,1,2]
