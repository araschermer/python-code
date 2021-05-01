from util import time_it


# Time complexity: O(N)
@time_it
def linear_search(list1: [], element) -> int:
    """Returns the index of a given element in a given sorted list, otherwise returns -1"""
    for index, item in enumerate(list1):
        if item == element:
            return index
    return -1


@time_it
def binary_search(list1: [], element) -> int:
    """Returns the index of a given element in a given sorted list , otherwise returns -1"""
    list_length = len(list1)
    left = 0
    right = list_length - 1
    while left <= right:
        middle = (left + right) // 2
        middle_element = list1[middle]
        if element == middle_element:
            return middle
        if element < middle_element:
            right = middle - 1
        else:
            left = middle + 1
    return -1


def binary_search_recursive(list1, element, left=0, right=None):
    if right is None:
        right = len(list1) - 1
    if right < left:
        return -1
    mid_index = (left + right) // 2

    mid_number = list1[mid_index]

    if mid_number == element:
        return mid_index

    if mid_number < element:
        left = mid_index + 1
    else:
        right = mid_index - 1

    return binary_search_recursive(list1, element, left, right)


if __name__ == "__main__":
    nums = [10, 23, 35, 87, 120, 940]
    linear_search([i for i in range(10000001)], 1000000)
    binary_search([i for i in range(10000001)], 1000000)
    for i in nums:
        print( binary_search_recursive(nums, i))
        print( binary_search_recursive(nums, i+1))