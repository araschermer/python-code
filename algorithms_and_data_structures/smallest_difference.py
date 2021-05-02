from algorithms_and_data_structures.util import check_validity


def smallest_difference(array1: [], array2: []) -> []:
    """find two numbers, one from each array, that has the smallest difference."""
    # Time Complexity: O(Nlog(N)+M(log(M))), for M as length of array1, and N as length of array2, or vise versa.
    check_validity(array1, repetitive_numbers=True, variable_types=[int, float])
    check_validity(array2,  repetitive_numbers=True, variable_types=[int, float])

    array1.sort()
    array2.sort()
    smallest_diff = float('inf')
    arr1_pointer = 0
    arr2_pointer = 0
    smallest_pair = []
    while arr1_pointer < len(array1) and arr2_pointer < len(array2):
        arr1_num = array1[arr1_pointer]
        arr2_num = array2[arr2_pointer]
        difference = abs(arr1_num - arr2_num)
        if arr1_num < arr2_num:
            arr1_pointer += 1
        elif arr1_num > arr2_num:
            arr2_pointer += 1
        elif arr1_num == arr2_num:
            smallest_pair = [arr1_num, arr2_num]
            return smallest_pair
        if smallest_diff > difference:
            smallest_diff = difference
            smallest_pair = [arr1_num, arr2_num]
    return smallest_pair


print(smallest_difference([-1, 5, 10, 30, 28, 2], [27, 122, 160, 13, 17]))
