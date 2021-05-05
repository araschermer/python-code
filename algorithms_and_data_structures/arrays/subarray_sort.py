from numpy.testing import assert_equal


def subarray_sort(array: []) -> [int]:
    """Returns the indices of the  minimum and subarray that needs to be sorted,
     in order to have the whole array sorted in an ascending order."""
    if type(array) is not list:
        raise TypeError("Invalid array type")
    min_to_sort = float('inf')
    max_to_sort = float('-inf')
    for index in range(len(array)):
        number = array[index]
        if type(number) is int or type(number) is float:
            pass
        else:
            raise TypeError(f"Invalid number type:{number}")
        if is_out_of_order(index, number, array):
            min_to_sort = min(min_to_sort, number)
            max_to_sort = max(max_to_sort, number)
    # If the array is already sorted, return [-1,-1]
    if min_to_sort == float('inf'):
        return [-1, -1]
    #  get the indices for the min and max values to be sorted
    start = 0
    #  start from the left  side of the array and find the first element that is not in the right order
    while min_to_sort >= array[start]:
        start += 1
    end = len(array) - 1
    # iterate backwards to find the first element that is not in the right order
    while max_to_sort <= array[end]:
        end -= 1
    #  return the indices of the minimum subarray that needs to be sorted
    return [start, end]


def is_out_of_order(index: int, number: float, array: [float]) -> bool:
    if index == 0:
        return number > array[index + 1]
    if index == len(array) - 1:
        return number < array[index - 1]
    return number > array[index + 1] or number < array[index - 1]

