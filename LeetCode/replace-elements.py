from nose.tools import assert_equal


def replace_elements(arr: [int]) -> [int]:
    """Given an array arr, replace every element in that array with the greatest element among the elements to its right
    and replace the last element with -1. After doing so, return the array."""
    if type(arr) is not list:
        raise TypeError("This method requires an input in a list ")
    for i in arr:
        if type(i) is int or type(i) is float:
            continue
        else:
            raise TypeError(f"{i} is neither an integer not a float")
    # If arr is empty, return arr
    if not arr:
        return arr
    # get the last index
    last_index = len(arr) - 1
    for index, num in enumerate(arr):
        # if the current index is the last index, replace the element ot the last index with -1 and return arr
        if index == last_index:
            arr[-1] = -1
            return arr
        # get the greatest element among the elements to the right of the current element
        next_greater = max(arr[index + 1:])
        # replace the current element with the greatest element to its right
        arr[index] = next_greater


if __name__ == "__main__":
    assert_equal(replace_elements(arr=[17, 18, 5, 4, 6, 1]), [18, 6, 6, 6, 1, -1])
    # Example 1:
    #
    # Input: arr = [17,18,5,4,6,1]
    # Output: [18,6,6,6,1,-1]
    # Explanation:
    # - index 0 --> the greatest element to the right of index 0 is index 1 (18).
    # - index 1 --> the greatest element to the right of index 1 is index 4 (6).
    # - index 2 --> the greatest element to the right of index 2 is index 4 (6).
    # - index 3 --> the greatest element to the right of index 3 is index 4 (6).
    # - index 4 --> the greatest element to the right of index 4 is index 5 (1).
    # - index 5 --> there are no elements to the right of index 5, so we put -1.
    assert_equal(replace_elements([400]), [-1])
    # Example 2:
    # Input: arr = [400]
    # Output: [-1]
    # Explanation: There are no elements to the right of index 0.
    # testing empty arr
    assert_equal(replace_elements([]), [])
