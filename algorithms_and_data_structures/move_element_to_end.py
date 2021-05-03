def move_elements_to_end(array: [], element) -> []:
    """Reorganizing the given array  and returning the same array
    with the elements  that match the given element value at the end of the array
    :param array: array of elements
    :param element: element of a given value"""
    # Time Complexity: O(n), Space Complexity:O(1)
    if array == [] or array is None:
        return []
    if element is None:
        raise TypeError("Element to move cannot be none")
    if element not in array:
        raise ValueError(f"No element:{element} exist in the Array:{array}")

    right_pointer = len(array) - 1

    left_pointer = 0
    while left_pointer < right_pointer:
        while array[right_pointer] == array[left_pointer]:
            right_pointer -= 1
        if array[left_pointer] == element:
            array[right_pointer], array[left_pointer] = array[left_pointer], array[right_pointer]
        left_pointer += 1
    return array

