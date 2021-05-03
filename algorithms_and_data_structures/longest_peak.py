def longest_peak(array: []) -> int:
    if type(array) is not list:
        raise TypeError("Invalid array type")
    for element in array:
        if type(element) is not int and type(element) is not float:
            raise TypeError("Invalid type of element")
    if len(array) < 2:
        return 0
    longest_peak_length = 0
    # The most right and the most left elements in the array cannot be a peak,
    # therefore they can be ignored in the for loop bound
    for index in range(1, len(array) - 1):

        # catching the potential peak
        if array[index - 1] < array[index] > array[index + 1]:
            left_pointer = right_pointer = index
            #  traversing the elements on the left side of the peak until decreasing number roll ends
            while array[left_pointer] > array[left_pointer - 1] and left_pointer > 0:
                left_pointer = left_pointer - 1
            # Traversing the elements on the right side of the peak  until the the decreasing order of the numbers break
            while array[right_pointer] > array[right_pointer + 1] and right_pointer < len(array):
                right_pointer = right_pointer + 1
            longest_peak_length = max(longest_peak_length, (right_pointer - left_pointer + 1))
    return longest_peak_length
