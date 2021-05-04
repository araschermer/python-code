def four_number_sum(array: [], target) -> []:
    result = []
    array.sort()
    first_pointer = 0
    second_pointer = 1
    third_pointer = 2
    fourth_pointer = len(array) - 1
    print(array)
    while first_pointer < fourth_pointer - 2:
        print([array[first_pointer], array[second_pointer],
               array[third_pointer], array[fourth_pointer]])

        numbers_sum = sum([array[first_pointer], array[second_pointer],
                           array[third_pointer], array[fourth_pointer]])
        print(numbers_sum)
        if numbers_sum == target:
            result.append([array[first_pointer], array[second_pointer],
                           array[third_pointer], array[fourth_pointer]])
            first_pointer += 1
            second_pointer = first_pointer + 1
            third_pointer = second_pointer + 1
        elif numbers_sum > target:
            fourth_pointer -= 1
        else:

            if third_pointer == fourth_pointer - 1 and second_pointer == third_pointer - 1:
                first_pointer += 1
                second_pointer = first_pointer + 1
                third_pointer = second_pointer + 1
            elif third_pointer == fourth_pointer - 1:
                second_pointer += 1
                third_pointer = second_pointer + 1
            elif third_pointer < fourth_pointer - 1:
                third_pointer += 1
    print(f'Result:{result}')
    return result


print(four_number_sum([7, 6, 4, -1, 1, 2], 16))
