class Solution(object):
    def twoSum(self, nums, target):
        """Given an array of integers nums and an integer target,
        return indices of the two numbers such that they add up to target
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        solution=[]
        sorted_nums=nums[:]
        sorted_nums.sort()
        first_pointer=0
        last_pointer=-1
        for n in range(len(sorted_nums)):
            first_number=sorted_nums[first_pointer]
            second_number=sorted_nums[last_pointer]
            if (first_number+second_number)>target:
                last_pointer-=1
                n-=1
            if (first_number+second_number)<target:
                first_pointer+=1
                n-=1
            if (first_number+second_number)==target:
                return[index for index in range(len(nums)) if nums[index] == sorted_nums[first_pointer]or nums[index] == sorted_nums[last_pointer]]