def monotonic_array(array: []) -> bool:
    """Returns True if the given array is monotonic, False otherwise.
    :param array: The array of a general direction, wither increasing or decreasing. order between all its elements
    a monotonic array can contain elements of the same value."""
    # Time Complexity: O(n), Space Complexity: O(1)
    check_valid_array(array)
    if len(array) <= 2:
        return True
    if array[0] >= array[1]: # If the array is sorted in a decreasing order
        for index in range(0, len(array) - 1):
            # If eny element breaks the pattern , then the array  is not monotonic
            if array[index] < array[index + 1]:
                return False

    elif array[0] <= array[1]: # If the array is sorted in an increasing order
        for index in range(0, len(array) - 1):
            # If eny element breaks the pattern , then the array  is not monotonic
            if array[index] > array[index + 1]:
                return False
    return True


def check_valid_array(array):
    if array is None or type(array) is not list:
        raise TypeError("Invalid array type")
    for element in array:
        if type(element) is int or type(element) is float:
            continue
        else:
            raise ValueError(f'element:{element} of type {type(element)}is not valid')
