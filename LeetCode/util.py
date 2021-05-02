def check_validity(nums, target):
    # Check valid target:
    if type(target) is not int:
        raise TypeError('Target is not an integer!')
    # check the type of the nums elements :
    for index, num in enumerate(nums):
        if type(num) is not int:
            raise TypeError(f"{num} Invalid number type in the input array")
        # check non-repetitiveness in the array
        if num in nums and nums.index(num) != index:
            raise ValueError("Array contains repetitive numbers")