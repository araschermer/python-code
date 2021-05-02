from time import time


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time()
        operation = func(*args, **kwargs)
        end = time()
        print(f"Runtime of {func.__name__} is: {(end - start) * 1000} ms")
        return operation

    return wrapper


def check_validity(nums, target=0, repetitive_numbers=False, variable_types=int):
    # Check valid target:
    if variable_types is None:
        variable_types = []
    if type(target) is not int:
        raise TypeError('Target is not an integer!')
    if nums is None or nums ==[]:
        raise TypeError("'NoneType' object is not iterable")
    # check the type of the nums elements :
    for index, num in enumerate(nums):
        if type(num) not in variable_types:
            raise TypeError(f"{num} Invalid number type in the input array")
        # check non-repetitiveness in the array
        if not repetitive_numbers:
            if num in nums and nums.index(num) != index:
                raise ValueError("Array contains repetitive numbers")
