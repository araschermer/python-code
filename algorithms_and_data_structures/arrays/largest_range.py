def find_largest_range(array: [float]):
    """Returns the largest range of numbers that exist in the array
    Time complexity: O(NlogN)
    Space complexity: O(1)"""
    current_range = 1
    max_range = 1
    upper_bound = array[0]
    array.sort()
    for index, number in enumerate(array):
        if number == array[index - 1]:
            #  if duplicate exists, do not increase range and continue
            continue
        if number == array[index - 1] + 1:
            #  if  number is in ascending with the previous numbers , increase range
            current_range += 1
            if current_range > max_range:
                # update max range
                max_range = current_range
                upper_bound = array[index]
        else:
            # otherwise, start over
            current_range = 1
    lower_bound = upper_bound - max_range + 1
    return [lower_bound, upper_bound]


def largest_range(array: [int]):
    # Time complexity: O(N)
    # Space complexity: O(N)
    largest_existing_range = []
    longest_range = 0
    numbers_table = {number: True for number in array}
    for number in array:
        if not numbers_table[number]:  # number already explored, and its value is set to False
            continue
        numbers_table[number] = False
        current_length = 1
        lower_bound = number - 1
        upper_bound = number + 1
        while lower_bound in numbers_table:
            numbers_table[lower_bound] = False
            current_length += 1
            lower_bound -= 1
        while upper_bound in numbers_table:
            numbers_table[upper_bound] = False
            current_length += 1
            upper_bound += 1
        if current_length > longest_range:
            longest_range = current_length
            largest_existing_range = [lower_bound + 1, upper_bound - 1]
    return largest_existing_range


if __name__ == '__main__':
    print(largest_range(array=[1, 0, 2, 3, -1, 4, 6]))
    print(largest_range(array=[1, 7, 5, 2, 3, 4, 6]))
    print(find_largest_range(array=[1, 0, 2, 3, -1, 4, 6]))
    print(find_largest_range(array=[1, 7, 5, 2, 3, 4, 6]))
